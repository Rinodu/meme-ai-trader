import unittest
from datetime import datetime, timedelta, timezone

from meme_ai_trader.validation import split


class ValidationSplitTests(unittest.TestCase):
    def test_split_keeps_holdout_separate(self):
        now = datetime(2026, 9, 16, 8, tzinfo=timezone.utc)
        development, validation, holdout = split([{"received_at": now + timedelta(days=2)}, {"received_at": now}, {"received_at": now + timedelta(days=1)}], now + timedelta(days=1), now + timedelta(days=2))
        self.assertEqual([now], [event["received_at"] for event in development])
        self.assertEqual([now + timedelta(days=1)], [event["received_at"] for event in validation])
        self.assertEqual([now + timedelta(days=2)], [event["received_at"] for event in holdout])
