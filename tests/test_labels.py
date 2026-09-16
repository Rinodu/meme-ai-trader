import unittest
from decimal import Decimal

from meme_ai_trader.labels import ExitPolicy, Outcome, label


class OutcomeLabelTests(unittest.TestCase):
    def test_labels_tp_sl_timeout_and_unavailable_route(self):
        policy = ExitPolicy(Decimal("0.1"), Decimal("0.1"), 2)
        self.assertEqual(Outcome.TP_FIRST, label(Decimal("10"), [Decimal("11"), Decimal("9")], policy))
        self.assertEqual(Outcome.SL_FIRST, label(Decimal("10"), [Decimal("9"), Decimal("11")], policy))
        self.assertEqual(Outcome.TIMEOUT, label(Decimal("10"), [Decimal("10"), Decimal("10")], policy))
        self.assertEqual(Outcome.EXIT_UNAVAILABLE, label(Decimal("10"), [], policy, False))
