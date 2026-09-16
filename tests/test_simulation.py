import unittest
from datetime import datetime, timezone
from decimal import Decimal

from meme_ai_trader.quotes import Quote
from meme_ai_trader.simulation import simulate


class SimulationTests(unittest.TestCase):
    def test_payload_must_match_quote_signer_and_destination(self):
        quote = Quote("SOL", "mint", Decimal("1"), Decimal("2"), datetime(2026, 9, 16, tzinfo=timezone.utc), True)
        payload = {"input_token": "SOL", "output_token": "mint", "input_amount": Decimal("1"), "min_output": Decimal("2"), "signer": "wallet", "destination": "ata"}
        self.assertTrue(simulate(payload, quote, "wallet", "ata"))
        self.assertFalse(simulate({**payload, "destination": "other"}, quote, "wallet", "ata"))
