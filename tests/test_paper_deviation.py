import unittest
from datetime import datetime, timedelta, timezone
from uuid import uuid4

from meme_ai_trader.labels import Outcome
from meme_ai_trader.paper_deviation import DeviationStatus, compare


class PaperDeviationTests(unittest.TestCase):
    def setUp(self):
        self.signal_id = uuid4()
        self.signal_time = datetime(2026, 1, 1, tzinfo=timezone.utc)

    def test_same_outcome_is_match(self):
        result = compare(self.signal_id, Outcome.TP_FIRST, Outcome.TP_FIRST, self.signal_time, self.signal_time + timedelta(minutes=5))
        self.assertEqual(DeviationStatus.MATCH, result.status)

    def test_different_outcome_is_deviation(self):
        result = compare(self.signal_id, Outcome.TP_FIRST, Outcome.SL_FIRST, self.signal_time, self.signal_time + timedelta(minutes=5))
        self.assertEqual(DeviationStatus.DEVIATION, result.status)

    def test_missing_outcome_is_insufficient(self):
        result = compare(self.signal_id, None, Outcome.TP_FIRST, self.signal_time, self.signal_time)
        self.assertEqual(DeviationStatus.INSUFFICIENT_DATA, result.status)

    def test_invalid_timestamp_is_insufficient(self):
        result = compare(self.signal_id, Outcome.TP_FIRST, Outcome.TP_FIRST, "not-a-timestamp", self.signal_time)
        self.assertEqual(DeviationStatus.INSUFFICIENT_DATA, result.status)

    def test_timestamp_outside_window_is_deviation(self):
        result = compare(self.signal_id, Outcome.TP_FIRST, Outcome.TP_FIRST, self.signal_time, self.signal_time + timedelta(hours=2))
        self.assertEqual(DeviationStatus.DEVIATION, result.status)
        self.assertIn("di luar", result.reason)
