from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class CostModel:
    fee_bps: Decimal
    slippage_bps: Decimal
    impact_bps: Decimal

    def estimate(self, notional: Decimal) -> Decimal:
        if notional < 0 or min(self.fee_bps, self.slippage_bps, self.impact_bps) < 0:
            raise ValueError("notional and costs must be non-negative")
        return notional * (self.fee_bps + self.slippage_bps + self.impact_bps) / Decimal("10000")
