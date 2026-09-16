import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from meme_ai_trader.quant import build


class FeatureTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 9, 16, 8, tzinfo=timezone.utc)

    def event(self, minutes, price, liquidity=100, volume=10):
        return {"received_at": self.now + timedelta(minutes=minutes), "price": price,
                "liquidity": liquidity, "volume_1h": volume}

    def test_uses_only_events_available_as_of(self):
        result = build([self.event(-2, 10), self.event(-1, 20), self.event(1, 100)], self.now, 2)
        self.assertTrue(result.ready)
        self.assertEqual(Decimal("1"), result.price_return)

    def test_warmup_and_zero_baseline_are_not_ready(self):
        self.assertEqual("INSUFFICIENT_PRICE_HISTORY", build([self.event(-1, 1)], self.now, 2).reason)
        self.assertEqual("ZERO_BASELINE_PRICE", build([self.event(-2, 0), self.event(-1, 1)], self.now, 2).reason)

    def test_missing_optional_data_is_not_converted_to_zero(self):
        result = build([self.event(-2, 10, None, 0), self.event(-1, 20, 200, 20)], self.now, 2)
        self.assertTrue(result.ready)
        self.assertIsNone(result.liquidity_change)
        self.assertIsNone(result.volume_acceleration)


if __name__ == "__main__":
    unittest.main()
