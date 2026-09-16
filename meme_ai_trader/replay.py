from collections.abc import Mapping
from datetime import datetime
from typing import Any

from meme_ai_trader.quant import FeatureSnapshot, build
from meme_ai_trader.strategy import Signal, SignalPolicy, evaluate


def replay(events: list[Mapping[str, Any]], warmup: int, policy: SignalPolicy) -> list[tuple[datetime, FeatureSnapshot, Signal]]:
    decisions = []
    for as_of in sorted({event["received_at"] for event in events}):
        features = build(events, as_of, warmup)
        decisions.append((as_of, features, evaluate(features, policy, as_of)))
    return decisions
