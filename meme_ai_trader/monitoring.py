"""Read-only health snapshot for Signal Bot operations."""

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


_SNAPSHOT = frozenset({"FRESH", "PARTIAL", "STALE", "MISSING", "INVALID"})


@dataclass(frozen=True)
class MonitoringReport:
    status: str
    alerts: tuple[str, ...]
    generated_at: datetime

    def as_dict(self) -> dict[str, Any]:
        return {"status": self.status, "alerts": list(self.alerts), "generated_at": self.generated_at.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")}


def monitor(snapshot_status: str, provider_ok: bool, telegram_ok: bool, audit_ok: bool, observed_at: datetime | None = None, now: datetime | None = None, max_age_seconds: int = 120) -> MonitoringReport:
    if snapshot_status not in _SNAPSHOT or not all(isinstance(value, bool) for value in (provider_ok, telegram_ok, audit_ok)) or max_age_seconds <= 0:
        raise ValueError("monitoring input tidak valid")
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    alerts: list[str] = []
    critical = not audit_ok or snapshot_status in {"MISSING", "INVALID"}
    if observed_at is not None:
        if observed_at.tzinfo is None or observed_at.utcoffset() is None:
            raise ValueError("observed_at harus timezone-aware")
        age = (current - observed_at.astimezone(timezone.utc)).total_seconds()
        if age < 0:
            critical = True
            alerts.append("SNAPSHOT_TIME_INVALID")
        elif age > max_age_seconds and snapshot_status == "FRESH":
            snapshot_status = "STALE"
    if snapshot_status == "PARTIAL":
        alerts.append("SNAPSHOT_PARTIAL")
    elif snapshot_status == "STALE":
        alerts.append("SNAPSHOT_STALE")
    elif snapshot_status == "MISSING":
        alerts.append("SNAPSHOT_MISSING")
    elif snapshot_status == "INVALID":
        alerts.append("SNAPSHOT_INVALID")
    if not provider_ok:
        alerts.append("PROVIDER_UNHEALTHY")
    if not telegram_ok:
        alerts.append("TELEGRAM_UNHEALTHY")
    if not audit_ok:
        alerts.append("AUDIT_FAILED")
    if critical:
        status = "CRITICAL"
    elif alerts:
        status = "DEGRADED"
    else:
        status = "HEALTHY"
    return MonitoringReport(status, tuple(alerts), current)
