"""Read-only recovery decision for operator runbooks."""

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class RecoveryAction(str, Enum):
    NO_ACTION = "NO_ACTION"
    PAUSE_ENTRIES = "PAUSE_ENTRIES"
    ESCALATE = "ESCALATE"


_STATUSES = frozenset({"OK", "STALE", "MISSING", "ERROR", "UNKNOWN"})


@dataclass(frozen=True)
class RecoveryDecision:
    incident_id: str
    action: RecoveryAction
    reasons: tuple[str, ...]
    generated_at: datetime

    def as_dict(self) -> dict[str, Any]:
        return {"incident_id": self.incident_id, "action": self.action.value, "reasons": list(self.reasons), "generated_at": self.generated_at.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")}


def decide_recovery(incident_id: str, data_status: str, provider_status: str, state_known: bool, retry_count: int, now: datetime | None = None) -> RecoveryDecision:
    if not incident_id.strip() or data_status not in _STATUSES or provider_status not in _STATUSES or not isinstance(state_known, bool) or not isinstance(retry_count, int) or retry_count < 0:
        raise ValueError("recovery input tidak valid")
    reasons: list[str] = []
    if not state_known or "UNKNOWN" in (data_status, provider_status):
        reasons.append("STATE_UNKNOWN")
        action = RecoveryAction.ESCALATE
    else:
        if data_status in {"STALE", "MISSING"}:
            reasons.append(f"DATA_{data_status}")
        if provider_status in {"STALE", "MISSING", "ERROR"}:
            reasons.append(f"PROVIDER_{provider_status}")
        action = RecoveryAction.PAUSE_ENTRIES if reasons else RecoveryAction.NO_ACTION
    return RecoveryDecision(incident_id, action, tuple(reasons), (now or datetime.now(timezone.utc)).astimezone(timezone.utc))
