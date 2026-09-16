import unittest
from uuid import uuid4

from meme_ai_trader.paper import forward


class PaperForwardTests(unittest.TestCase):
    def test_forward_creates_paper_signal_only(self):
        signal = forward(uuid4(), "mint")
        self.assertEqual("mint", signal.mint)
