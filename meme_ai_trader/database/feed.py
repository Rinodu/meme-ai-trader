from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any

from .raw_events import RawEventRepository


REQUIRED_FIELDS = ("price", "liquidity")


@dataclass(frozen=True)
class FeedAssessment:
    available: bool
    ready: bool
    stale: bool
    missing_fields: tuple[str, ...]


def _utc(value: datetime, name: str) -> datetime:
    if value.utcoffset() is None:
        raise ValueError(f"{name} must be timezone-aware")
    return value.astimezone(timezone.utc)


def assess(event: Mapping[str, Any] | None, as_of: datetime, max_age: timedelta) -> FeedAssessment:
    if max_age <= timedelta():
        raise ValueError("max_age must be positive")
    as_of = _utc(as_of, "as_of")
    if event is None:
        return FeedAssessment(False, False, False, REQUIRED_FIELDS)
    received_at = event.get("received_at")
    if not isinstance(received_at, datetime):
        raise ValueError("received_at must be a datetime")
    stale = _utc(received_at, "received_at") < as_of - max_age
    missing = tuple(field for field in REQUIRED_FIELDS if event.get(field) is None)
    return FeedAssessment(True, not stale and not missing, stale, missing)


def reconcile(
    repository: RawEventRepository,
    chain_id: str,
    mint_address: str,
    as_of: datetime,
    max_age: timedelta,
) -> FeedAssessment:
    return assess(repository.latest_for_mint(chain_id, mint_address, as_of), as_of, max_age)
