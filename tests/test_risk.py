import unittest
from decimal import Decimal
from meme_ai_trader.risk import SizingPolicy, size

class SizingTests(unittest.TestCase):
    def test_caps_exposure_and_fee_reserve(self):
        policy = SizingPolicy(Decimal("0.01"), Decimal("100"), Decimal("300"), Decimal("10"))
        self.assertEqual(Decimal("100"), size(Decimal("1000"), Decimal("0.05"), Decimal("0"), policy))
        self.assertEqual(Decimal("20"), size(Decimal("1000"), Decimal("0.05"), Decimal("280"), policy))
        self.assertEqual(Decimal("0"), size(Decimal("1000"), Decimal("0.05"), Decimal("300"), policy))

if __name__ == "__main__":
    unittest.main()
