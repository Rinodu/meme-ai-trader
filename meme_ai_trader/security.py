"""Read-only security-provider boundary and fail-closed gate."""

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import StrEnum
from typing import Any, Protocol


class SecurityStatus(StrEnum):
    PASS = "PASS"
    REJECT = "REJECT"
    UNKNOWN = "UNKNOWN"


class SecurityProviderError(RuntimeError):
    """A provider did not return usable security evidence."""


class SecurityProvider(Protocol):
    def inspect(self, chain_id: str, mint_address: str) -> Mapping[str, Any]: ...


@dataclass(frozen=True)
class SecurityPolicy:
    max_evidence_age: timedelta
    rule_version: str

    def __post_init__(self) -> None:
        if self.max_evidence_age <= timedelta():
            raise ValueError("max_evidence_age must be positive")
        if not self.rule_version.strip():
            raise ValueError("rule_version must not be blank")


@dataclass(frozen=True)
class SecurityDecision:
    status: SecurityStatus
    reasons: tuple[str, ...]
    evidence: Mapping[str, Any] | None
    checked_at: datetime | None
    rule_version: str

    @property
    def entry_allowed(self) -> bool:
        return self.status is SecurityStatus.PASS


def _utc(value: Any, name: str) -> datetime:
    if not isinstance(value, datetime) or value.utcoffset() is None:
        raise ValueError(f"{name} must be a timezone-aware datetime")
    return value.astimezone(timezone.utc)


def assess(evidence: Mapping[str, Any] | None, policy: SecurityPolicy, as_of: datetime) -> SecurityDecision:
    """Classify provider evidence; missing, stale, or partial evidence is UNKNOWN."""
    as_of = _utc(as_of, "as_of")
    if evidence is None:
        return SecurityDecision(SecurityStatus.UNKNOWN, ("NO_EVIDENCE",), None, None, policy.rule_version)
    checked_at = evidence.get("checked_at")
    if not isinstance(checked_at, datetime) or checked_at.utcoffset() is None:
        return SecurityDecision(SecurityStatus.UNKNOWN, ("EVIDENCE_TIME_INVALID",), evidence, None, policy.rule_version)
    checked_at = _utc(checked_at, "checked_at")
    if checked_at > as_of or checked_at < as_of - policy.max_evidence_age:
        return SecurityDecision(SecurityStatus.UNKNOWN, ("EVIDENCE_STALE",), evidence, checked_at, policy.rule_version)

    required = ("source", "slot", "mint_authority_disabled", "freeze_authority_disabled", "program_supported", "tradable")
    missing = tuple(f"MISSING_{field.upper()}" for field in required if evidence.get(field) is None)
    if missing:
        return SecurityDecision(SecurityStatus.UNKNOWN, missing, evidence, checked_at, policy.rule_version)

    failures = tuple(
        reason for field, reason in (
            ("mint_authority_disabled", "MINT_AUTHORITY_ACTIVE"),
            ("freeze_authority_disabled", "FREEZE_AUTHORITY_ACTIVE"),
            ("program_supported", "PROGRAM_UNSUPPORTED"),
            ("tradable", "NOT_TRADABLE"),
        ) if evidence[field] is not True
    )
    status = SecurityStatus.REJECT if failures else SecurityStatus.PASS
    return SecurityDecision(status, failures, evidence, checked_at, policy.rule_version)


def inspect(provider: SecurityProvider, chain_id: str, mint_address: str, policy: SecurityPolicy, as_of: datetime) -> SecurityDecision:
    """Read provider evidence once; provider failures always fail closed as UNKNOWN."""
    try:
        evidence = provider.inspect(chain_id, mint_address)
    except SecurityProviderError:
        return SecurityDecision(SecurityStatus.UNKNOWN, ("PROVIDER_ERROR",), None, None, policy.rule_version)
    return assess(evidence, policy, as_of)
