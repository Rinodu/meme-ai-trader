import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from meme_ai_trader.discovery import UniversePolicy, evaluate


class UniverseFilterTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 9, 15, 8, tzinfo=timezone.utc)
        self.policy = UniversePolicy(
            chain_id="solana-mainnet",
            allowed_token_programs=frozenset({"spl-token"}),
            max_feed_age=timedelta(minutes=2),
            min_token_age=timedelta(minutes=5),
            min_liquidity=Decimal("1000"),
            min_volume_1h=Decimal("500"),
        )
        self.candidate = {
            "chain_id": "solana-mainnet", "mint_address": "mint", "pool_address": "pool",
            "token_program": "spl-token", "token_created_at": self.now - timedelta(minutes=5),
            "received_at": self.now, "price": 0, "liquidity": Decimal("1000"), "volume_1h": Decimal("500"),
        }

    def test_complete_fresh_candidate_at_thresholds_is_eligible(self):
        result = evaluate(self.candidate, self.policy, self.now)
        self.assertTrue(result.eligible)
        self.assertEqual((), result.reasons)

    def test_candidate_is_rejected_with_explicit_reasons(self):
        result = evaluate({**self.candidate, "pool_address": "", "token_program": "unknown",
                           "token_created_at": self.now - timedelta(minutes=1),
                           "received_at": self.now - timedelta(minutes=3), "liquidity": None,
                           "volume_1h": Decimal("499")}, self.policy, self.now)
        self.assertFalse(result.eligible)
        self.assertEqual(("MISSING_POOL_ADDRESS", "TOKEN_PROGRAM_NOT_ALLOWED", "FEED_NOT_READY",
                          "TOKEN_TOO_NEW", "LIQUIDITY_BELOW_MINIMUM", "VOLUME_BELOW_MINIMUM"), result.reasons)

    def test_unknown_or_future_token_age_blocks_candidate(self):
        unknown = evaluate({**self.candidate, "token_created_at": None}, self.policy, self.now)
        future = evaluate({**self.candidate, "token_created_at": self.now + timedelta(seconds=1)}, self.policy, self.now)
        self.assertIn("TOKEN_AGE_UNKNOWN", unknown.reasons)
        self.assertIn("TOKEN_AGE_UNKNOWN", future.reasons)


if __name__ == "__main__":
    unittest.main()
