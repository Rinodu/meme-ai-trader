import unittest
from datetime import datetime, timedelta, timezone

from meme_ai_trader.database.feed import REQUIRED_FIELDS, assess


class FeedAssessmentTests(unittest.TestCase):
    def test_fresh_zero_values_are_ready(self):
        now = datetime(2026, 9, 15, 8, tzinfo=timezone.utc)
        result = assess({"received_at": now, "price": 0, "liquidity": 0}, now, timedelta(minutes=1))
        self.assertTrue(result.ready)
        self.assertFalse(result.stale)

    def test_stale_partial_and_missing_feed_are_not_ready(self):
        now = datetime(2026, 9, 15, 8, tzinfo=timezone.utc)
        stale = assess({"received_at": now - timedelta(minutes=2), "price": 1, "liquidity": 1}, now, timedelta(minutes=1))
        partial = assess({"received_at": now, "price": 1, "liquidity": None}, now, timedelta(minutes=1))
        absent = assess(None, now, timedelta(minutes=1))
        self.assertTrue(stale.stale)
        self.assertEqual(("liquidity",), partial.missing_fields)
        self.assertEqual(REQUIRED_FIELDS, absent.missing_fields)


if __name__ == "__main__":
    unittest.main()
