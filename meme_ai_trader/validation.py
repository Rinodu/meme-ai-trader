from collections.abc import Mapping
from datetime import datetime
from typing import Any


def split(events: list[Mapping[str, Any]], validation_start: datetime, holdout_start: datetime) -> tuple[list[Mapping[str, Any]], list[Mapping[str, Any]], list[Mapping[str, Any]]]:
    if validation_start >= holdout_start:
        raise ValueError("validation must precede holdout")
    ordered = sorted(events, key=lambda event: event["received_at"])
    return (
        [event for event in ordered if event["received_at"] < validation_start],
        [event for event in ordered if validation_start <= event["received_at"] < holdout_start],
        [event for event in ordered if event["received_at"] >= holdout_start],
    )
