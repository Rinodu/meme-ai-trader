from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class ReportStatus(str, Enum):
    INCONCLUSIVE = "INCONCLUSIVE"


@dataclass(frozen=True)
class StressReport:
    expectancy: Decimal
    profit_factor: Decimal | None
    max_drawdown: Decimal
    status: ReportStatus = ReportStatus.INCONCLUSIVE


def report(pnl: list[Decimal]) -> StressReport:
    if not pnl:
        raise ValueError("pnl is required")
    gains = sum((value for value in pnl if value > 0), Decimal())
    losses = -sum((value for value in pnl if value < 0), Decimal())
    equity = peak = drawdown = Decimal()
    for value in pnl:
        equity += value
        peak = max(peak, equity)
        drawdown = min(drawdown, equity - peak)
    return StressReport(sum(pnl, Decimal()) / len(pnl), None if not losses else gains / losses, -drawdown)
