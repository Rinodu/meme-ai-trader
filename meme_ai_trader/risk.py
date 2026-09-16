from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class SizingPolicy:
    risk_per_trade: Decimal
    position_cap: Decimal
    portfolio_cap: Decimal
    fee_reserve: Decimal


def size(equity: Decimal, loss_fraction: Decimal, exposure: Decimal, policy: SizingPolicy) -> Decimal:
    if equity < 0 or not 0 < loss_fraction <= 1 or not 0 <= policy.risk_per_trade <= 1:
        raise ValueError("invalid sizing input")
    risk_notional = equity * policy.risk_per_trade / loss_fraction
    available = max(Decimal(), min(policy.portfolio_cap - exposure, equity - policy.fee_reserve))
    return max(Decimal(), min(risk_notional, policy.position_cap, available))
