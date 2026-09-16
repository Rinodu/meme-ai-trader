import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from meme_ai_trader.replay import replay
from meme_ai_trader.strategy import SignalPolicy

class ReplayTests(unittest.TestCase):
    def test_replay_is_point_in_time_and_deterministic(self):
        now = datetime(2026, 9, 16, 8, tzinfo=timezone.utc)
        events = [{"received_at": now, "price": 10}, {"received_at": now + timedelta(minutes=1), "price": 20}, {"received_at": now + timedelta(minutes=2), "price": 1}]
        first = replay(events, 2, SignalPolicy(Decimal("0.5"), timedelta(minutes=1)))
        self.assertEqual(first, replay(events, 2, SignalPolicy(Decimal("0.5"), timedelta(minutes=1))))
        self.assertEqual([False, True, False], [item[2].eligible for item in first])

    def test_replay_orders_late_input_by_received_time(self):
        now = datetime(2026, 9, 16, 8, tzinfo=timezone.utc)
        events = [{"received_at": now + timedelta(minutes=2), "price": 40}, {"received_at": now, "price": 10}, {"received_at": now + timedelta(minutes=1), "price": 20}]
        result = replay(events, 2, SignalPolicy(Decimal("0.5"), timedelta(minutes=1)))
        self.assertEqual([now, now + timedelta(minutes=1), now + timedelta(minutes=2)], [item[0] for item in result])
        self.assertFalse(result[0][2].eligible)
