"""Point-in-time candidate filtering for the discovery universe."""

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation
from typing import Any

from .database.feed import FeedAssessment, assess


@dataclass(frozen=True)
class UniversePolicy:
    chain_id: str
    allowed_token_programs: frozenset[str]
    max_feed_age: timedelta
    min_token_age: timedelta
    min_liquidity: Decimal
    min_volume_1h: Decimal

    def __post_init__(self) -> None:
        if not self.chain_id.strip():
            raise ValueError("chain_id must not be blank")
        if not self.allowed_token_programs:
            raise ValueError("allowed_token_programs must not be empty")
        if self.max_feed_age <= timedelta() or self.min_token_age < timedelta():
            raise ValueError("ages must be non-negative and max_feed_age must be positive")
        if self.min_liquidity < 0 or self.min_volume_1h < 0:
            raise ValueError("minimums must be non-negative")


@dataclass(frozen=True)
class UniverseDecision:
    eligible: bool
    reasons: tuple[str, ...]
    feed: FeedAssessment


def _utc(value: Any, name: str) -> datetime:
    if not isinstance(value, datetime) or value.utcoffset() is None:
        raise ValueError(f"{name} must be a timezone-aware datetime")
    return value.astimezone(timezone.utc)


def _decimal(value: Any, name: str) -> Decimal | None:
    if value is None:
        return None
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise ValueError(f"{name} must be numeric") from error
    if not result.is_finite() or result < 0:
        raise ValueError(f"{name} must be a non-negative finite number")
    return result


def evaluate(candidate: Mapping[str, Any], policy: UniversePolicy, as_of: datetime) -> UniverseDecision:
    """Evaluate one candidate using only values available at ``as_of``."""
    as_of = _utc(as_of, "as_of")
    feed = assess(candidate, as_of, policy.max_feed_age)
    reasons: list[str] = []

    if candidate.get("chain_id") != policy.chain_id:
        reasons.append("CHAIN_MISMATCH")
    for field in ("mint_address", "pool_address"):
        if not isinstance(candidate.get(field), str) or not candidate[field].strip():
            reasons.append(f"MISSING_{field.upper()}")
    if candidate.get("token_program") not in policy.allowed_token_programs:
        reasons.append("TOKEN_PROGRAM_NOT_ALLOWED")
    if not feed.ready:
        reasons.append("FEED_NOT_READY")

    created_at = candidate.get("token_created_at")
    if created_at is None:
        reasons.append("TOKEN_AGE_UNKNOWN")
    else:
        created_at = _utc(created_at, "token_created_at")
        if created_at > as_of:
            reasons.append("TOKEN_AGE_UNKNOWN")
        elif as_of - created_at < policy.min_token_age:
            reasons.append("TOKEN_TOO_NEW")

    liquidity = _decimal(candidate.get("liquidity"), "liquidity")
    if liquidity is None or liquidity < policy.min_liquidity:
        reasons.append("LIQUIDITY_BELOW_MINIMUM")
    volume = _decimal(candidate.get("volume_1h"), "volume_1h")
    if volume is None or volume < policy.min_volume_1h:
        reasons.append("VOLUME_BELOW_MINIMUM")
    return UniverseDecision(not reasons, tuple(reasons), feed)
