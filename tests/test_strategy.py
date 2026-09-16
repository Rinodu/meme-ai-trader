import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from meme_ai_trader.quant import FeatureSnapshot
from meme_ai_trader.strategy import SignalPolicy, active, evaluate


class SignalTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 9, 16, 8, tzinfo=timezone.utc)
        self.policy = SignalPolicy(Decimal("0.1"), timedelta(minutes=5))

    def features(self, ready=True, price_return=Decimal("0.1")):
        return FeatureSnapshot(ready, None if ready else "INSUFFICIENT_PRICE_HISTORY", 2, price_return, None, None)

    def test_eligible_signal_has_deterministic_expiry(self):
        signal = evaluate(self.features(), self.policy, self.now)
        self.assertTrue(signal.eligible)
        self.assertEqual(self.now + timedelta(minutes=5), signal.expires_at)
        self.assertTrue(active(signal, self.now))

    def test_unready_and_below_threshold_features_are_rejected(self):
        self.assertEqual("FEATURES:INSUFFICIENT_PRICE_HISTORY", evaluate(self.features(False), self.policy, self.now).reason)
        self.assertEqual("PRICE_RETURN_BELOW_THRESHOLD", evaluate(self.features(True, Decimal("0.09")), self.policy, self.now).reason)

    def test_expired_signal_is_not_active(self):
        signal = evaluate(self.features(), self.policy, self.now)
        self.assertFalse(active(signal, self.now + timedelta(minutes=5)))


if __name__ == "__main__":
    unittest.main()
