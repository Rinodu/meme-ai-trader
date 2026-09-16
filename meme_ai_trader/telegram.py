from dataclasses import dataclass, replace
from datetime import datetime
from decimal import Decimal
from uuid import UUID


def allowed(sender_id: int, command: str, senders: frozenset[int], commands: frozenset[str]) -> bool:
    return sender_id in senders and command in commands


@dataclass(frozen=True)
class Approval:
    intent_id: UUID
    token: str
    side: str
    amount: Decimal
    expires_at: datetime
    used: bool = False

    def consume(self, now: datetime, intent_id: UUID, token: str, side: str, amount: Decimal) -> "Approval | None":
        if self.used or now >= self.expires_at or (self.intent_id, self.token, self.side, self.amount) != (intent_id, token, side, amount):
            return None
        return replace(self, used=True)
