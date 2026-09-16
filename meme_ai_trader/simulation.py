from collections.abc import Mapping
from decimal import Decimal
from typing import Any

from .quotes import Quote


def simulate(payload: Mapping[str, Any], quote: Quote, authority: str, destination: str) -> bool:
    return (
        payload.get("input_token") == quote.input_token
        and payload.get("output_token") == quote.output_token
        and payload.get("input_amount") == quote.input_amount
        and isinstance(payload.get("min_output"), Decimal)
        and payload.get("min_output") >= quote.min_output
        and payload.get("authority") == authority
        and payload.get("destination") == destination
    )
