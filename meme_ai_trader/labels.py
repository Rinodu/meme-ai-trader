from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class Outcome(str, Enum):
    TP_FIRST = "TP_FIRST"
    SL_FIRST = "SL_FIRST"
    TIMEOUT = "TIMEOUT"
    EXIT_UNAVAILABLE = "EXIT_UNAVAILABLE"
    DATA_INSUFFICIENT = "DATA_INSUFFICIENT"


@dataclass(frozen=True)
class ExitPolicy:
    take_profit: Decimal
    stop_loss: Decimal
    observations: int


def label(entry_price: Decimal, prices: list[Decimal], policy: ExitPolicy, route_available: bool = True) -> Outcome:
    if entry_price <= 0 or policy.take_profit <= 0 or policy.stop_loss <= 0 or policy.observations <= 0:
        raise ValueError("prices and observations must be positive")
    if not route_available:
        return Outcome.EXIT_UNAVAILABLE
    if len(prices) < policy.observations:
        return Outcome.DATA_INSUFFICIENT
    for price in prices[:policy.observations]:
        if price >= entry_price * (1 + policy.take_profit):
            return Outcome.TP_FIRST
        if price <= entry_price * (1 - policy.stop_loss):
            return Outcome.SL_FIRST
    return Outcome.TIMEOUT
