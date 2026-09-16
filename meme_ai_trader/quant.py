from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any

from meme_ai_trader.database.raw_events import RawEventRepository


@dataclass(frozen=True)
class FeatureSnapshot:
    ready: bool
    reason: str | None
    sample_count: int
    price_return: Decimal | None
    liquidity_change: Decimal | None
    volume_acceleration: Decimal | None


def _change(first: Any, last: Any) -> Decimal | None:
    if first is None or last is None:
        return None
    first, last = Decimal(str(first)), Decimal(str(last))
    return None if first == 0 else last / first - 1


def build(events: list[Mapping[str, Any]], as_of: datetime, warmup: int) -> FeatureSnapshot:
    if warmup < 2:
        raise ValueError("warmup must be at least 2")
    available = [event for event in events if event["received_at"] <= as_of and event.get("price") is not None]
    window = available[-warmup:]
    if len(window) < warmup:
        return FeatureSnapshot(False, "INSUFFICIENT_PRICE_HISTORY", len(window), None, None, None)
    price_return = _change(window[0]["price"], window[-1]["price"])
    if price_return is None:
        return FeatureSnapshot(False, "ZERO_BASELINE_PRICE", len(window), None, None, None)
    return FeatureSnapshot(
        True, None, len(window), price_return,
        _change(window[0].get("liquidity"), window[-1].get("liquidity")),
        _change(window[0].get("volume_1h"), window[-1].get("volume_1h")),
    )


def for_mint(
    repository: RawEventRepository, chain_id: str, mint_address: str, as_of: datetime, warmup: int
) -> FeatureSnapshot:
    return build(repository.available_for_mint(chain_id, mint_address, as_of), as_of, warmup)
