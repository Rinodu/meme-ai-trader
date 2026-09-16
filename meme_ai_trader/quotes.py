from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal


@dataclass(frozen=True)
class Quote:
    input_token: str
    output_token: str
    input_amount: Decimal
    min_output: Decimal
    quoted_at: datetime
    route_available: bool


def usable(quote: Quote, now: datetime, max_age: timedelta) -> bool:
    return quote.route_available and quote.input_amount > 0 and quote.min_output > 0 and now >= quote.quoted_at and now - quote.quoted_at <= max_age
