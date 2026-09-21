from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from enum import Enum
from typing import Any


class QualityStatus(str, Enum):
    VALID = "VALID"
    INCONCLUSIVE = "INCONCLUSIVE"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


_VALID_OUTCOMES = frozenset({"MATCH", "DEVIATION", "INSUFFICIENT_DATA"})
_SIX_PLACES = Decimal("0.000001")


@dataclass(frozen=True)
class QualityReport:
    report_id: str
    status: QualityStatus
    sample_count: int
    valid_sample_count: int
    match_count: int
    deviation_count: int
    deviation_ratio: Decimal | None
    data_coverage: Decimal | None
    drawdown: Decimal | None
    expectancy: Decimal | None
    calibration_summary: dict[str, Any] | None
    probability_available: bool
    limitations: tuple[str, ...]
    generated_at: datetime

    def as_dict(self) -> dict[str, Any]:
        number = lambda value: None if value is None else float(value)
        return {
            "report_id": self.report_id,
            "status": self.status.value,
            "sample_count": self.sample_count,
            "valid_sample_count": self.valid_sample_count,
            "match_count": self.match_count,
            "deviation_count": self.deviation_count,
            "deviation_ratio": number(self.deviation_ratio),
            "data_coverage": number(self.data_coverage),
            "drawdown": number(self.drawdown),
            "expectancy": number(self.expectancy),
            "calibration_summary": self.calibration_summary,
            "probability_available": self.probability_available,
            "limitations": list(self.limitations),
            "generated_at": self.generated_at.isoformat().replace("+00:00", "Z"),
        }


def _timestamp(value: datetime | str, field: str) -> datetime:
    if isinstance(value, str):
        try:
            value = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError as error:
            raise ValueError(f"{field} must be a valid ISO-8601 timestamp") from error
    if not isinstance(value, datetime) or value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{field} must be timezone-aware")
    return value.astimezone(timezone.utc)


def _decimal(value: Any, field: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{field} must be numeric")
    try:
        result = value if isinstance(value, Decimal) else Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as error:
        raise ValueError(f"{field} must be numeric") from error
    if not result.is_finite():
        raise ValueError(f"{field} must be finite")
    return result


def _ratio(numerator: int, denominator: int) -> Decimal | None:
    if denominator == 0:
        return None
    return (Decimal(numerator) / Decimal(denominator)).quantize(_SIX_PLACES, rounding=ROUND_HALF_UP)


def _status_value(value: Any) -> str:
    return value.value if isinstance(value, Enum) else value


def _probability_summary(
    data: Mapping[str, Any] | None,
    valid_sample_count: int,
    minimum_sample: int,
    limitations: list[str],
) -> tuple[dict[str, Any] | None, bool]:
    if data is None:
        limitations.append("data probabilitas tidak tersedia")
        return None, False
    if not isinstance(data, Mapping):
        raise ValueError("probability_data must be a mapping")
    values = data.get("values", [])
    if isinstance(values, (str, bytes)) or not isinstance(values, Sequence):
        raise ValueError("probability_data.values must be a sequence")
    for index, value in enumerate(values):
        parsed = _decimal(value, f"probability_data.values[{index}]")
        if not Decimal("0") <= parsed <= Decimal("1"):
            raise ValueError("probability values must be between 0 and 1")
    out_of_sample = data.get("out_of_sample", False)
    calibrated = data.get("calibrated", False)
    if not isinstance(out_of_sample, bool) or not isinstance(calibrated, bool):
        raise ValueError("probability calibration flags must be boolean")
    method = data.get("calibration_method")
    eligible = valid_sample_count >= minimum_sample and bool(values) and out_of_sample and calibrated and bool(method)
    if eligible:
        return {
            "status": "CALIBRATED",
            "method": str(method),
            "value_count": len(values),
            "out_of_sample": True,
        }, True
    reasons = []
    if valid_sample_count < minimum_sample:
        reasons.append(f"sample valid di bawah minimum {minimum_sample}")
    if not values:
        reasons.append("nilai probabilitas tidak tersedia")
    if not out_of_sample:
        reasons.append("evaluasi out-of-sample belum tersedia")
    if not calibrated:
        reasons.append("kalibrasi belum terdokumentasi")
    if not method:
        reasons.append("metode kalibrasi belum didokumentasikan")
    summary: dict[str, Any] = {"status": "UNAVAILABLE", "reason": "; ".join(reasons)}
    for key in ("score", "evidence_quality"):
        if key in data:
            summary[key] = data[key]
    limitations.append("probabilitas prediktif tidak ditampilkan: " + summary["reason"])
    return summary, False


def build_quality_report(
    report_id: str,
    started_at: datetime | str,
    ended_at: datetime | str,
    outcomes: Sequence[Mapping[str, Any]],
    sample_count: int,
    valid_sample_count: int | None = None,
    metrics: Mapping[str, Any] | None = None,
    probability_data: Mapping[str, Any] | None = None,
    minimum_sample: int = 30,
    generated_at: datetime | str | None = None,
) -> QualityReport:
    if not isinstance(report_id, str) or not report_id.strip():
        raise ValueError("report_id is required")
    if isinstance(sample_count, bool) or not isinstance(sample_count, int) or sample_count < 0:
        raise ValueError("sample_count must be a non-negative integer")
    if isinstance(minimum_sample, bool) or not isinstance(minimum_sample, int) or minimum_sample <= 0:
        raise ValueError("minimum_sample must be a positive integer")
    if isinstance(outcomes, (str, bytes)) or not isinstance(outcomes, Sequence):
        raise ValueError("outcomes must be a sequence")
    started = _timestamp(started_at, "started_at")
    ended = _timestamp(ended_at, "ended_at")
    if started > ended:
        raise ValueError("started_at must not be after ended_at")
    if sample_count < len(outcomes):
        raise ValueError("sample_count cannot be lower than outcome records")

    seen_ids: set[str] = set()
    match_count = deviation_count = 0
    for record in outcomes:
        if not isinstance(record, Mapping):
            raise ValueError("each outcome must be a mapping")
        signal_id = record.get("signal_id")
        if not isinstance(signal_id, str) or not signal_id.strip():
            raise ValueError("each outcome requires signal_id")
        if signal_id in seen_ids:
            raise ValueError("duplicate signal_id in outcomes")
        seen_ids.add(signal_id)
        timestamp = _timestamp(record.get("timestamp"), "outcome timestamp")
        if not started <= timestamp <= ended:
            raise ValueError("outcome timestamp must be inside report period")
        status = _status_value(record.get("status"))
        if status not in _VALID_OUTCOMES:
            raise ValueError(f"unknown outcome label: {status!r}")
        if status == "MATCH":
            match_count += 1
        elif status == "DEVIATION":
            deviation_count += 1

    calculated_valid = match_count + deviation_count
    if valid_sample_count is not None:
        if isinstance(valid_sample_count, bool) or not isinstance(valid_sample_count, int) or valid_sample_count < 0:
            raise ValueError("valid_sample_count must be a non-negative integer")
        if valid_sample_count != calculated_valid:
            raise ValueError("valid_sample_count does not match outcome labels")
    else:
        valid_sample_count = calculated_valid
    if valid_sample_count > sample_count:
        raise ValueError("valid_sample_count cannot exceed sample_count")

    limitations: list[str] = []
    if valid_sample_count == 0:
        status = QualityStatus.INSUFFICIENT_DATA
        limitations.append("tidak ada outcome valid")
    elif valid_sample_count < minimum_sample:
        status = QualityStatus.INCONCLUSIVE
        limitations.append(f"sample valid di bawah minimum {minimum_sample}")
    else:
        status = QualityStatus.VALID
    if sample_count == 0:
        limitations.append("sample_count nol; data coverage tidak dapat dihitung")
    elif valid_sample_count < sample_count:
        limitations.append("sebagian outcome tidak valid atau tidak tersedia")

    drawdown = expectancy = None
    if metrics is not None:
        if not isinstance(metrics, Mapping):
            raise ValueError("metrics must be a mapping")
        if metrics.get("drawdown") is not None:
            drawdown = _decimal(metrics["drawdown"], "drawdown")
        else:
            limitations.append("drawdown tidak tersedia")
        if metrics.get("expectancy") is not None:
            expectancy = _decimal(metrics["expectancy"], "expectancy")
        else:
            limitations.append("expectancy tidak tersedia")
    else:
        limitations.extend(("drawdown tidak tersedia", "expectancy tidak tersedia"))

    calibration_summary, probability_available = _probability_summary(
        probability_data, valid_sample_count, minimum_sample, limitations
    )
    generated = _timestamp(generated_at, "generated_at") if generated_at is not None else datetime.now(timezone.utc)
    return QualityReport(
        report_id=report_id,
        status=status,
        sample_count=sample_count,
        valid_sample_count=valid_sample_count,
        match_count=match_count,
        deviation_count=deviation_count,
        deviation_ratio=_ratio(deviation_count, valid_sample_count),
        data_coverage=_ratio(valid_sample_count, sample_count),
        drawdown=drawdown,
        expectancy=expectancy,
        calibration_summary=calibration_summary,
        probability_available=probability_available,
        limitations=tuple(limitations),
        generated_at=generated,
    )
