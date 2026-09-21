"""Minimal pre-operation audit for Signal Bot."""

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from meme_ai_trader.config import SAFE_MODES, Settings
from meme_ai_trader.signer import ExecutionStatus, status as boundary_status


@dataclass(frozen=True)
class AuditReport:
    status: str
    checks: dict[str, str]
    reasons: tuple[str, ...]
    generated_at: datetime

    def as_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "checks": dict(self.checks),
            "reasons": list(self.reasons),
            "generated_at": self.generated_at.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
        }


def audit_signal_only(settings: Settings, data_ready: bool, allowlist_ready: bool, now: datetime | None = None) -> AuditReport:
    checks = {
        "mode": "PASS" if settings.mode in SAFE_MODES else "FAIL",
        "execution_boundary": "PASS" if boundary_status() is ExecutionStatus.DISABLED else "FAIL",
        "data": "PASS" if data_ready is True else "FAIL",
        "allowlist": "PASS" if allowlist_ready is True else "FAIL",
    }
    reasons = tuple(f"{name.upper()}_CHECK_FAILED" for name, value in checks.items() if value == "FAIL")
    return AuditReport("PASS" if not reasons else "FAIL", checks, reasons, (now or datetime.now(timezone.utc)).astimezone(timezone.utc))
