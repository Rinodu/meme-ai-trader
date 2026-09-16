from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True)
class PaperOrder:
    intent_id: UUID
    token: str
    side: str
    amount: Decimal
    status: str = "PAPER"


def forward(intent_id: UUID, token: str, side: str, amount: Decimal) -> PaperOrder:
    if not token or side not in {"BUY", "SELL"} or amount <= 0:
        raise ValueError("invalid paper order")
    return PaperOrder(intent_id, token, side, amount)
