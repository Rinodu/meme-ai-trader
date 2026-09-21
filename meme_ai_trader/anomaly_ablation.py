from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from enum import StrEnum
from typing import Any

from .labels import Outcome
from .onchain_snapshot import OnChainSnapshot, SnapshotStatus
from .quality_report import QualityStatus


class AnomalyCode(StrEnum):
    TOP_HOLDER_RATIO_HIGH = "ANOMALY_TOP_HOLDER_RATIO_HIGH"
    LIQUIDITY_BELOW_THRESHOLD = "ANOMALY_LIQUIDITY_BELOW_THRESHOLD"
    ACTIVE_MINT_AUTHORITY = "ANOMALY_ACTIVE_MINT_AUTHORITY"
    ACTIVE_FREEZE_AUTHORITY = "ANOMALY_ACTIVE_FREEZE_AUTHORITY"
    LIQUIDITY_NOT_LOCKED = "ANOMALY_LIQUIDITY_NOT_LOCKED"


@dataclass(frozen=True)
class AnomalyRules:
    rule_version: str
    max_top_holder_ratio: Decimal | None = None
    min_liquidity: Decimal | None = None
    reject_active_authorities: bool = False
    require_liquidity_locked: bool = False
    minimum_labeled: int = 30

    def __post_init__(self) -> None:
        if not isinstance(self.rule_version, str) or not self.rule_version.strip():
            raise ValueError("rule_version is required")
        if self.max_top_holder_ratio is not None and not 0 <= self.max_top_holder_ratio <= 1:
            raise ValueError("max_top_holder_ratio must be between 0 and 1")
        if self.min_liquidity is not None and self.min_liquidity < 0:
            raise ValueError("min_liquidity must be non-negative")
        if not isinstance(self.reject_active_authorities, bool) or not isinstance(self.require_liquidity_locked, bool):
            raise ValueError("anomaly flags must be boolean")
        if isinstance(self.minimum_labeled, bool) or not isinstance(self.minimum_labeled, int) or self.minimum_labeled <= 0:
            raise ValueError("minimum_labeled must be positive")


@dataclass(frozen=True)
class CandidateObservation:
    candidate_id: str
    decision_time: datetime
    snapshot: OnChainSnapshot
    baseline_eligible: bool
    outcome: Outcome | str | None = None
    cost: Decimal | str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.candidate_id, str) or not self.candidate_id.strip():
            raise ValueError("candidate_id is required")
        if not isinstance(self.decision_time, datetime) or self.decision_time.tzinfo is None or self.decision_time.utcoffset() is None:
            raise ValueError("decision_time must be timezone-aware")
        if not isinstance(self.baseline_eligible, bool):
            raise ValueError("baseline_eligible must be boolean")
        if self.outcome is not None:
            value = self.outcome.value if isinstance(self.outcome, Outcome) else self.outcome
            if value not in {item.value for item in Outcome}:
                raise ValueError(f"unknown outcome: {value!r}")
        if self.cost is not None:
            try:
                cost = self.cost if isinstance(self.cost, Decimal) else Decimal(str(self.cost))
            except (InvalidOperation, ValueError, TypeError) as error:
                raise ValueError("cost must be numeric") from error
            if not cost.is_finite() or cost < 0:
                raise ValueError("cost must be finite and non-negative")


@dataclass(frozen=True)
class FilterDecision:
    candidate_id: str
    observed_at: datetime | None
    rule_version: str
    data_status: SnapshotStatus
    passed: bool
    reasons: tuple[str, ...]
    anomaly_codes: tuple[AnomalyCode, ...]


@dataclass(frozen=True)
class ModeMetrics:
    signal_count: int
    labeled_count: int
    tp_first_count: int
    tp_first_ratio: Decimal | None
    total_cost: Decimal | None
    average_cost: Decimal | None


@dataclass(frozen=True)
class AblationReport:
    rule_version: str
    status: QualityStatus
    candidate_count: int
    baseline: ModeMetrics
    baseline_plus_filter: ModeMetrics
    coverage_baseline: Decimal | None
    coverage_baseline_plus_filter: Decimal | None
    rejected_by_reason: dict[str, dict[str, int]]
    outcomes_lost_to_filter: tuple[dict[str, str], ...]
    limitations: tuple[str, ...]
    generated_at: datetime

    def as_dict(self) -> dict[str, Any]:
        def metric(value: Decimal | None) -> float | None:
            return None if value is None else float(value)

        def mode(value: ModeMetrics) -> dict[str, Any]:
            return {
                "signal_count": value.signal_count,
                "labeled_count": value.labeled_count,
                "tp_first_count": value.tp_first_count,
                "tp_first_ratio": metric(value.tp_first_ratio),
                "total_cost": metric(value.total_cost),
                "average_cost": metric(value.average_cost),
            }

        return {
            "rule_version": self.rule_version,
            "status": self.status.value,
            "candidate_count": self.candidate_count,
            "baseline": mode(self.baseline),
            "baseline_plus_filter": mode(self.baseline_plus_filter),
            "coverage_baseline": metric(self.coverage_baseline),
            "coverage_baseline_plus_filter": metric(self.coverage_baseline_plus_filter),
            "rejected_by_reason": self.rejected_by_reason,
            "outcomes_lost_to_filter": list(self.outcomes_lost_to_filter),
            "limitations": list(self.limitations),
            "generated_at": self.generated_at.isoformat().replace("+00:00", "Z"),
        }


def _utc(value: datetime, field: str) -> datetime:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{field} must be timezone-aware")
    return value.astimezone(timezone.utc)


def _outcome(value: Outcome | str | None) -> str | None:
    if value is None:
        return None
    return value.value if isinstance(value, Outcome) else value


def _ratio(numerator: int, denominator: int) -> Decimal | None:
    if denominator == 0:
        return None
    return (Decimal(numerator) / Decimal(denominator)).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)


def _data_reasons(candidate: CandidateObservation) -> tuple[str, ...]:
    decision_time = _utc(candidate.decision_time, "decision_time")
    reasons: list[str] = []
    if candidate.snapshot.observed_at is not None and _utc(candidate.snapshot.observed_at, "observed_at") > decision_time:
        reasons.append("DATA_LEAKAGE")
    if not candidate.snapshot.allows_signal():
        reasons.append("DATA_NOT_READY")
    if not candidate.baseline_eligible:
        reasons.append("BASELINE_INELIGIBLE")
    return tuple(reasons)


def evaluate_candidate(candidate: CandidateObservation, rules: AnomalyRules) -> FilterDecision:
    """Evaluate only snapshot data available at decision time."""
    reasons = list(_data_reasons(candidate))
    anomalies: list[AnomalyCode] = []
    snapshot = candidate.snapshot
    if not reasons:
        if rules.max_top_holder_ratio is not None:
            if snapshot.top_holder_ratio is None:
                reasons.append("DATA_NOT_READY")
            elif snapshot.top_holder_ratio > rules.max_top_holder_ratio:
                anomalies.append(AnomalyCode.TOP_HOLDER_RATIO_HIGH)
        if rules.min_liquidity is not None:
            if snapshot.liquidity is None:
                reasons.append("DATA_NOT_READY")
            elif snapshot.liquidity < rules.min_liquidity:
                anomalies.append(AnomalyCode.LIQUIDITY_BELOW_THRESHOLD)
        if rules.reject_active_authorities:
            if snapshot.mint_authority is not None:
                anomalies.append(AnomalyCode.ACTIVE_MINT_AUTHORITY)
            if snapshot.freeze_authority is not None:
                anomalies.append(AnomalyCode.ACTIVE_FREEZE_AUTHORITY)
        if rules.require_liquidity_locked:
            if snapshot.liquidity_locked is None:
                reasons.append("DATA_NOT_READY")
            elif snapshot.liquidity_locked is False:
                anomalies.append(AnomalyCode.LIQUIDITY_NOT_LOCKED)
    reasons.extend(code.value for code in anomalies)
    return FilterDecision(
        candidate.candidate_id,
        snapshot.observed_at,
        rules.rule_version,
        snapshot.data_status,
        not reasons,
        tuple(dict.fromkeys(reasons)),
        tuple(anomalies),
    )


def _mode_metrics(candidates: Sequence[CandidateObservation]) -> ModeMetrics:
    valid = [candidate for candidate in candidates if _outcome(candidate.outcome) is not None]
    tp_first = sum(_outcome(candidate.outcome) == Outcome.TP_FIRST.value for candidate in valid)
    costs = [candidate.cost if isinstance(candidate.cost, Decimal) else Decimal(str(candidate.cost)) for candidate in candidates if candidate.cost is not None]
    total_cost = sum(costs, Decimal()) if costs else None
    return ModeMetrics(
        signal_count=len(candidates),
        labeled_count=len(valid),
        tp_first_count=tp_first,
        tp_first_ratio=_ratio(tp_first, len(valid)),
        total_cost=total_cost,
        average_cost=(total_cost / len(costs) if costs else None),
    )


def _rejections(reasons_by_candidate: Mapping[str, tuple[str, ...]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for reasons in reasons_by_candidate.values():
        counts.update(reasons or ("NO_REASON",))
    return dict(sorted(counts.items()))


def evaluate_ablation(
    candidates: Sequence[CandidateObservation],
    rules: AnomalyRules,
    generated_at: datetime | None = None,
) -> AblationReport:
    if isinstance(candidates, (str, bytes)) or not isinstance(candidates, Sequence):
        raise ValueError("candidates must be a sequence")
    seen: set[str] = set()
    baseline_candidates: list[CandidateObservation] = []
    filtered_candidates: list[CandidateObservation] = []
    baseline_reasons: dict[str, tuple[str, ...]] = {}
    filtered_reasons: dict[str, tuple[str, ...]] = {}
    for candidate in candidates:
        if candidate.candidate_id in seen:
            raise ValueError("duplicate candidate_id")
        seen.add(candidate.candidate_id)
        decision = evaluate_candidate(candidate, rules)
        baseline_ok = not _data_reasons(candidate)
        if baseline_ok:
            baseline_candidates.append(candidate)
        else:
            baseline_reasons[candidate.candidate_id] = _data_reasons(candidate)
        if baseline_ok and decision.passed:
            filtered_candidates.append(candidate)
        elif not baseline_ok:
            filtered_reasons[candidate.candidate_id] = _data_reasons(candidate)
        else:
            filtered_reasons[candidate.candidate_id] = decision.reasons

    baseline = _mode_metrics(baseline_candidates)
    filtered = _mode_metrics(filtered_candidates)
    lost = tuple(
        {"candidate_id": candidate.candidate_id, "outcome": _outcome(candidate.outcome)}
        for candidate in baseline_candidates
        if candidate.candidate_id not in {item.candidate_id for item in filtered_candidates} and candidate.outcome is not None
    )
    if not candidates or baseline.signal_count == 0:
        status = QualityStatus.INSUFFICIENT_DATA
    elif baseline.labeled_count < rules.minimum_labeled or filtered.labeled_count < rules.minimum_labeled:
        status = QualityStatus.INCONCLUSIVE
    else:
        status = QualityStatus.VALID
    limitations = ["filtered-mode metrics are subject to selection bias"]
    if baseline.labeled_count < rules.minimum_labeled or filtered.labeled_count < rules.minimum_labeled:
        limitations.append(f"labeled sample below minimum {rules.minimum_labeled}")
    if not baseline_candidates:
        limitations.append("no baseline signal after safety/data gate")
    if lost:
        limitations.append(f"{len(lost)} labeled outcome(s) lost to filter")
    generated = _utc(generated_at, "generated_at") if generated_at is not None else datetime.now(timezone.utc)
    return AblationReport(
        rules.rule_version,
        status,
        len(candidates),
        baseline,
        filtered,
        _ratio(baseline.signal_count, len(candidates)),
        _ratio(filtered.signal_count, len(candidates)),
        {"baseline": _rejections(baseline_reasons), "baseline_plus_filter": _rejections(filtered_reasons)},
        lost,
        tuple(limitations),
        generated,
    )
