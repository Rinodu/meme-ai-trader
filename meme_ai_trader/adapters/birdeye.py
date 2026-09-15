import json
from collections.abc import Callable, Mapping
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from uuid import uuid4

from meme_ai_trader.database.feed import FeedAssessment, assess
from meme_ai_trader.database.raw_events import RawEventRepository


class BirdeyeError(RuntimeError):
    pass


class BirdeyeClient:
    _URL = "https://public-api.birdeye.so/defi/token_overview"

    def __init__(self, api_key: str, opener: Callable[..., Any] = urlopen) -> None:
        if not api_key:
            raise ValueError("Birdeye API key is required")
        self._api_key = api_key
        self._opener = opener

    def token_overview(self, mint_address: str) -> dict[str, Any]:
        if not mint_address.strip():
            raise ValueError("mint_address is required")
        request = Request(
            f"{self._URL}?{urlencode({'address': mint_address})}",
            headers={"Accept": "application/json", "X-API-KEY": self._api_key, "x-chain": "solana"},
        )
        try:
            with self._opener(request, timeout=10) as response:
                if response.status != 200:
                    raise BirdeyeError(f"Birdeye request failed ({response.status})")
                payload = json.loads(response.read())
        except (HTTPError, URLError) as error:
            raise BirdeyeError(f"Birdeye request failed ({getattr(error, 'code', 'network')})") from error
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise BirdeyeError("Birdeye returned invalid JSON") from error

        if not isinstance(payload, dict) or payload.get("success") is not True:
            raise BirdeyeError("Birdeye returned an unsuccessful response")
        data = payload.get("data")
        if not isinstance(data, dict):
            raise BirdeyeError("Birdeye response data must be an object")
        return data


def _decimal(snapshot: Mapping[str, Any], provider_name: str, event_name: str) -> Decimal | None:
    value = snapshot.get(provider_name)
    if value is None:
        return None
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise BirdeyeError(f"Birdeye {provider_name} must be numeric") from error
    if not number.is_finite():
        raise BirdeyeError(f"Birdeye {provider_name} must be finite")
    if event_name not in {"price_change_1h"} and number < 0:
        raise BirdeyeError(f"Birdeye {provider_name} must not be negative")
    return number


def raw_event(
    mint_address: str, snapshot: Mapping[str, Any], received_at: datetime
) -> dict[str, Any]:
    """Map one Birdeye snapshot without guessing an event identity or time."""
    if not mint_address.strip():
        raise ValueError("mint_address is required")
    fields = {
        "price": ("price", "price"),
        "market_cap": ("mc", "market_cap"),
        "fdv": ("fdv", "fdv"),
        "liquidity": ("liquidity", "liquidity"),
        "volume_1h": ("v1hUSD", "volume_1h"),
        "buy_count": ("buy1h", "buy_count"),
        "sell_count": ("sell1h", "sell_count"),
        "price_change_1h": ("priceChange1hPercent", "price_change_1h"),
    }
    values = {event_name: _decimal(snapshot, provider_name, event_name)
              for event_name, (provider_name, _) in fields.items()}
    missing = [event_name for event_name, (provider_name, _) in fields.items()
               if snapshot.get(provider_name) is None]
    return {
        "event_id": uuid4(),
        "source": "birdeye",
        "schema_version": 1,
        "chain_id": "solana",
        "mint_address": mint_address,
        "event_time": None,
        "received_at": received_at,
        "data_quality_status": "PARTIAL" if missing else "COMPLETE",
        "missing_fields": missing,
        "raw_payload": dict(snapshot),
        **values,
    }


def collect_snapshot(
    client: BirdeyeClient,
    repository: RawEventRepository,
    mint_address: str,
    received_at: datetime,
    max_age: timedelta,
) -> tuple[int, FeedAssessment]:
    event = raw_event(mint_address, client.token_overview(mint_address), received_at)
    return repository.insert(event), assess(event, received_at, max_age)
