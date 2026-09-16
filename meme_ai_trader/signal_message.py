from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SignalMessage:
    mint: str
    symbol: str | None
    reason: str
    evidence: str
    entry_zone: str
    invalidation: str
    target: str
    exit_recommendation: str
    max_hold: str
    early_exit: str
    expires_at: datetime
    signal_score: str
    evidence_quality: str


def format_signal(signal: SignalMessage) -> str:
    name = f" ({signal.symbol})" if signal.symbol else ""
    return (
        f"SIGNAL {signal.mint}{name}\nAlasan: {signal.reason}\nBukti: {signal.evidence}\n"
        f"Entry: {signal.entry_zone}\nInvalidation/stop: {signal.invalidation}\nTarget: {signal.target}\n"
        f"Exit: {signal.exit_recommendation}\nMaks hold: {signal.max_hold}\nExit awal: {signal.early_exit}\n"
        f"Kedaluwarsa: {signal.expires_at.isoformat()}\nSignal score: {signal.signal_score}; "
        f"evidence quality: {signal.evidence_quality} (bukan probabilitas profit)"
    )
