"""Fail-closed entry gate and immutable decision audit record."""

from dataclasses import dataclass
from datetime import datetime, timezone

from .discovery import UniverseDecision
from .security import SecurityDecision, SecurityStatus


@dataclass(frozen=True)
class EntryGateDecision:
    allowed: bool
    reasons: tuple[str, ...]
    evaluated_at: datetime
    universe: UniverseDecision
    security: SecurityDecision


def decide(universe: UniverseDecision, security: SecurityDecision, as_of: datetime) -> EntryGateDecision:
    """Permit entry only when both upstream gates explicitly pass."""
    if as_of.utcoffset() is None:
        raise ValueError("as_of must be timezone-aware")
    reasons = tuple(f"UNIVERSE:{reason}" for reason in universe.reasons)
    if security.status is not SecurityStatus.PASS:
        reasons += (f"SECURITY:{security.status}",)
        reasons += tuple(f"SECURITY:{reason}" for reason in security.reasons)
    return EntryGateDecision(not reasons, reasons, as_of.astimezone(timezone.utc), universe, security)
