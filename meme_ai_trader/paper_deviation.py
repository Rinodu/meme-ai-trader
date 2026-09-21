from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import StrEnum
from uuid import UUID

from .labels import Outcome


class DeviationStatus(StrEnum):
    MATCH = "MATCH"
    DEVIATION = "DEVIATION"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


@dataclass(frozen=True)
class PaperDeviation:
    signal_id: str
    status: DeviationStatus
    reason: str


def _timestamp(value: datetime | str | None) -> datetime | None:
    if isinstance(value, str):
        try:
            value = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    if not isinstance(value, datetime) or value.tzinfo is None:
        return None
    return value.astimezone(timezone.utc)


def compare(
    signal_id: UUID | str | None,
    signal_outcome: Outcome | str | None,
    paper_outcome: Outcome | str | None,
    signal_timestamp: datetime | str | None,
    paper_timestamp: datetime | str | None,
    window_seconds: int = 3600,
) -> PaperDeviation:
    """Compare one signal outcome with its paper outcome in a bounded window."""
    identifier = str(signal_id) if signal_id else ""
    signal_time = _timestamp(signal_timestamp)
    paper_time = _timestamp(paper_timestamp)
    valid_outcomes = {item.value for item in Outcome}
    if (
        not identifier
        or signal_outcome not in valid_outcomes
        or paper_outcome not in valid_outcomes
        or signal_time is None
        or paper_time is None
        or not isinstance(window_seconds, int)
        or window_seconds <= 0
    ):
        return PaperDeviation(identifier, DeviationStatus.INSUFFICIENT_DATA, "outcome, timestamp, signal_id, atau window tidak valid")
    if not signal_time <= paper_time <= signal_time + timedelta(seconds=window_seconds):
        return PaperDeviation(identifier, DeviationStatus.DEVIATION, "paper timestamp berada di luar signal window")
    if signal_outcome == paper_outcome:
        return PaperDeviation(identifier, DeviationStatus.MATCH, "outcome sama dalam signal window")
    return PaperDeviation(identifier, DeviationStatus.DEVIATION, "outcome sinyal dan paper berbeda")
