import unittest
from decimal import Decimal
from uuid import uuid4

from meme_ai_trader.paper import forward


class PaperForwardTests(unittest.TestCase):
    def test_forward_creates_paper_record_only(self):
        order = forward(uuid4(), "mint", "BUY", Decimal("10"))
        self.assertEqual("PAPER", order.status)
        self.assertEqual("BUY", order.side)
