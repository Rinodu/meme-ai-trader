"""Bounded, optional narrative enrichment for read-only Signal Bot."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, TimeoutError
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from enum import Enum
from hashlib import sha256
from typing import Any, Protocol

from meme_ai_trader.onchain_snapshot import _valid_address


class SocialStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    MISSING = "MISSING"
    STALE = "STALE"
    INVALID = "INVALID"
    DUPLICATE = "DUPLICATE"


class NarrativeStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    CACHE_HIT = "CACHE_HIT"
    DISABLED = "DISABLED"
    UNAVAILABLE = "UNAVAILABLE"


@dataclass(frozen=True)
class SocialEvidence:
    mint_address: str
    source: str
    source_id: str
    published_at: datetime
    received_at: datetime
    text: str
    data_status: SocialStatus = SocialStatus.AVAILABLE

    def __post_init__(self) -> None:
        if isinstance(self.data_status, str):
            try:
                object.__setattr__(self, "data_status", SocialStatus(self.data_status))
            except ValueError as error:
                raise ValueError("data_status tidak valid") from error
        if not _valid_address(self.mint_address):
            raise ValueError("mint_address tidak valid")
        if not self.source.strip() or not self.source_id.strip():
            raise ValueError("source dan source_id wajib diisi")
        for name, value in (("published_at", self.published_at), ("received_at", self.received_at)):
            if isinstance(value, str):
                try:
                    value = datetime.fromisoformat(value.replace("Z", "+00:00"))
                except ValueError as error:
                    raise ValueError(f"{name} harus timestamp ISO-8601") from error
                object.__setattr__(self, name, value)
            if value.tzinfo is None or value.utcoffset() is None:
                raise ValueError(f"{name} harus timezone-aware")
        if not isinstance(self.text, str) or not self.text.strip():
            raise ValueError("text wajib diisi")
        if len(self.text) > 4000:
            raise ValueError("text melebihi batas 4000 karakter")


@dataclass(frozen=True)
class NarrativeConfig:
    enabled: bool = False
    monthly_budget_idr: Decimal = Decimal("0")
    future_budget_ceiling_idr: Decimal = Decimal("50000")
    max_calls_per_month: int = 0
    timeout_seconds: float = 5.0
    max_retries: int = 1
    cache_ttl_seconds: int = 900
    max_output_chars: int = 2000
    prompt_version: str = "m12.3-v1"
    model: str = "fixture-none"

    def __post_init__(self) -> None:
        if self.monthly_budget_idr < 0 or self.max_calls_per_month < 0:
            raise ValueError("budget dan call cap tidak boleh negatif")
        if self.monthly_budget_idr > self.future_budget_ceiling_idr:
            raise ValueError("budget melampaui ceiling M12.3")
        if self.enabled and self.monthly_budget_idr > 0 and self.max_calls_per_month <= 0:
            raise ValueError("mode aktif wajib memiliki call cap")
        if self.timeout_seconds <= 0 or not 0 <= self.max_retries <= 1:
            raise ValueError("timeout/retry di luar batas")
        if self.cache_ttl_seconds <= 0 or self.max_output_chars <= 0:
            raise ValueError("cache TTL/output bound harus positif")


@dataclass(frozen=True)
class ProviderNarrative:
    summary: str
    catalyst_status: str = "unknown"
    evidence_refs: tuple[str, ...] = ()
    uncertainties: tuple[str, ...] = ()
    cost_idr: Decimal | None = None


class NarrativeProvider(Protocol):
    def estimate_cost_idr(self, evidence: SocialEvidence) -> Decimal | None: ...

    def complete(self, evidence: SocialEvidence, timeout_seconds: float) -> ProviderNarrative: ...


@dataclass(frozen=True)
class NarrativeResult:
    mint_address: str
    status: NarrativeStatus
    narrative_summary: str | None
    catalyst_status: str
    evidence_refs: tuple[str, ...]
    uncertainties: tuple[str, ...]
    generated_at: datetime
    expires_at: datetime
    prompt_version: str
    probability_available: bool = False
    reason: str | None = None

    def as_dict(self) -> dict[str, Any]:
        iso = lambda value: value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        return {
            "mint_address": self.mint_address,
            "status": self.status.value,
            "narrative_summary": self.narrative_summary,
            "catalyst_status": self.catalyst_status,
            "evidence_refs": list(self.evidence_refs),
            "uncertainties": list(self.uncertainties),
            "generated_at": iso(self.generated_at),
            "expires_at": iso(self.expires_at),
            "prompt_version": self.prompt_version,
            "probability_available": False,
            "reason": self.reason,
        }


class NarrativeService:
    def __init__(self, config: NarrativeConfig | None = None, provider: NarrativeProvider | None = None) -> None:
        self.config = config or NarrativeConfig()
        self.provider = provider
        self._cache: dict[str, NarrativeResult] = {}
        self._seen: set[tuple[str, str]] = set()
        self._calls = 0
        self._spent = Decimal("0")

    def analyze(self, evidence: SocialEvidence, now: datetime | None = None) -> NarrativeResult:
        now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
        key = (evidence.source, evidence.source_id)
        if evidence.data_status is not SocialStatus.AVAILABLE:
            return self._unavailable(evidence, now, f"DATA_{evidence.data_status.value}")
        cache_key = self._cache_key(evidence)
        cached = self._cache.get(cache_key)
        if cached and cached.expires_at > now:
            return NarrativeResult(**{**cached.__dict__, "status": NarrativeStatus.CACHE_HIT})
        if key in self._seen:
            return self._unavailable(evidence, now, "DUPLICATE")
        self._seen.add(key)
        if not self.config.enabled or self.config.monthly_budget_idr <= 0:
            return self._unavailable(evidence, now, "LLM_DISABLED_BUDGET_ZERO", NarrativeStatus.DISABLED)
        if self.provider is None:
            return self._unavailable(evidence, now, "NO_PROVIDER")
        if self.config.max_calls_per_month and self._calls >= self.config.max_calls_per_month:
            return self._unavailable(evidence, now, "CALL_CAP_EXHAUSTED")
        estimate = self._money(self.provider.estimate_cost_idr(evidence))
        if estimate is None:
            return self._unavailable(evidence, now, "COST_UNKNOWN")
        if estimate > self.config.monthly_budget_idr - self._spent:
            return self._unavailable(evidence, now, "BUDGET_EXHAUSTED")
        result = None
        for _ in range(self.config.max_retries + 1):
            self._calls += 1
            try:
                with ThreadPoolExecutor(max_workers=1) as pool:
                    result = pool.submit(self.provider.complete, evidence, self.config.timeout_seconds).result(
                        timeout=self.config.timeout_seconds
                    )
                break
            except (TimeoutError, Exception):
                result = None
        if result is None:
            return self._unavailable(evidence, now, "PROVIDER_FAILURE_OR_TIMEOUT")
        actual = self._money(result.cost_idr)
        if actual is None or actual > self.config.monthly_budget_idr - self._spent or len(result.summary) > self.config.max_output_chars:
            return self._unavailable(evidence, now, "ACTUAL_COST_UNKNOWN_OR_OUTPUT_INVALID")
        if not result.summary.strip() or not set(result.evidence_refs).issubset({evidence.source_id}):
            return self._unavailable(evidence, now, "PROVIDER_SCHEMA_INVALID")
        self._spent += actual
        output = NarrativeResult(
            evidence.mint_address, NarrativeStatus.AVAILABLE, result.summary, result.catalyst_status,
            result.evidence_refs, result.uncertainties, now,
            now + timedelta(seconds=self.config.cache_ttl_seconds), self.config.prompt_version,
        )
        self._cache[cache_key] = output
        return output

    def _cache_key(self, evidence: SocialEvidence) -> str:
        raw = "|".join((evidence.mint_address, self.config.model, self.config.prompt_version, evidence.source_id, evidence.text))
        return sha256(raw.encode()).hexdigest()

    def _unavailable(self, evidence: SocialEvidence, now: datetime, reason: str, status: NarrativeStatus = NarrativeStatus.UNAVAILABLE) -> NarrativeResult:
        return NarrativeResult(evidence.mint_address, status, None, "unknown", (), (reason,), now, now, self.config.prompt_version, False, reason)

    @staticmethod
    def _money(value: Any) -> Decimal | None:
        if value is None or isinstance(value, bool):
            return None
        try:
            value = value if isinstance(value, Decimal) else Decimal(str(value))
        except (InvalidOperation, ValueError, TypeError):
            return None
        return value if value.is_finite() and value >= 0 else None
