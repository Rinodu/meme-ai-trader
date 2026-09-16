import unittest
from datetime import datetime, timedelta, timezone

from meme_ai_trader.security import (
    SecurityPolicy,
    SecurityProviderError,
    SecurityStatus,
    assess,
    inspect,
)


class SecurityGateTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 9, 15, 8, tzinfo=timezone.utc)
        self.policy = SecurityPolicy(timedelta(minutes=2), "m3.2")
        self.evidence = {
            "source": "fixture", "slot": 1, "checked_at": self.now,
            "mint_authority_disabled": True, "freeze_authority_disabled": True,
            "program_supported": True, "tradable": True,
        }

    def test_complete_fresh_safe_evidence_passes(self):
        result = assess(self.evidence, self.policy, self.now)
        self.assertEqual(SecurityStatus.PASS, result.status)
        self.assertTrue(result.entry_allowed)
        self.assertEqual("m3.2", result.rule_version)

    def test_failed_controls_reject_with_each_reason(self):
        result = assess({**self.evidence, "mint_authority_disabled": False, "tradable": False}, self.policy, self.now)
        self.assertEqual(SecurityStatus.REJECT, result.status)
        self.assertEqual(("MINT_AUTHORITY_ACTIVE", "NOT_TRADABLE"), result.reasons)
        self.assertFalse(result.entry_allowed)

    def test_missing_or_stale_evidence_is_unknown(self):
        missing = assess(None, self.policy, self.now)
        stale = assess({**self.evidence, "checked_at": self.now - timedelta(minutes=3)}, self.policy, self.now)
        partial = assess({**self.evidence, "slot": None}, self.policy, self.now)
        self.assertEqual(SecurityStatus.UNKNOWN, missing.status)
        self.assertEqual(SecurityStatus.UNKNOWN, stale.status)
        self.assertEqual(("MISSING_SLOT",), partial.reasons)

    def test_provider_error_is_unknown(self):
        class FailingProvider:
            def inspect(self, chain_id, mint_address):
                raise SecurityProviderError("timeout")

        result = inspect(FailingProvider(), "solana-mainnet", "mint", self.policy, self.now)
        self.assertEqual(SecurityStatus.UNKNOWN, result.status)
        self.assertEqual(("PROVIDER_ERROR",), result.reasons)


if __name__ == "__main__":
    unittest.main()
