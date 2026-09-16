from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal

from meme_ai_trader.quant import FeatureSnapshot


@dataclass(frozen=True)
class SignalPolicy:
    min_price_return: Decimal
    ttl: timedelta


@dataclass(frozen=True)
class Signal:
    eligible: bool
    reason: str | None
    expires_at: datetime | None


def evaluate(features: FeatureSnapshot, policy: SignalPolicy, as_of: datetime) -> Signal:
    if policy.ttl <= timedelta():
        raise ValueError("ttl must be positive")
    if not features.ready:
        return Signal(False, f"FEATURES:{features.reason}", None)
    if features.price_return is None:
        return Signal(False, "PRICE_RETURN_MISSING", None)
    if features.price_return < policy.min_price_return:
        return Signal(False, "PRICE_RETURN_BELOW_THRESHOLD", None)
    return Signal(True, None, as_of + policy.ttl)


def active(signal: Signal, as_of: datetime) -> bool:
    return signal.eligible and signal.expires_at is not None and as_of < signal.expires_at
