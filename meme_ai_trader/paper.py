from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class PaperSignal:
    signal_id: UUID
    mint: str
    status: str = "PAPER"


def forward(signal_id: UUID, mint: str) -> PaperSignal:
    if not mint:
        raise ValueError("mint is required")
    return PaperSignal(signal_id, mint)
