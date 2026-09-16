import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from meme_ai_trader.quotes import Quote, usable


class QuoteTests(unittest.TestCase):
    def test_route_and_age_are_required(self):
        now = datetime(2026, 9, 16, 8, tzinfo=timezone.utc)
        quote = Quote("SOL", "mint", Decimal("1"), Decimal("2"), now, True)
        self.assertTrue(usable(quote, now, timedelta(seconds=1)))
        self.assertFalse(usable(Quote("SOL", "mint", Decimal("1"), Decimal("2"), now, False), now, timedelta(seconds=1)))
        self.assertFalse(usable(quote, now + timedelta(seconds=2), timedelta(seconds=1)))
