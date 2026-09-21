import unittest
from decimal import Decimal

from meme_ai_trader.costs import CostModel


class CostModelTests(unittest.TestCase):
    def test_estimates_explicit_fee_slippage_and_impact(self):
        model = CostModel(Decimal("10"), Decimal("20"), Decimal("5"))
        self.assertEqual(Decimal("0.35"), model.estimate(Decimal("100")))
        with self.assertRaises(ValueError):
            model.estimate(Decimal("-1"))
