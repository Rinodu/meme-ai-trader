import unittest
from datetime import datetime, timezone

from meme_ai_trader.database.feed import FeedAssessment
from meme_ai_trader.discovery import UniverseDecision
from meme_ai_trader.entry_gate import decide
from meme_ai_trader.security import SecurityDecision, SecurityStatus


class EntryGateTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 9, 15, 8, tzinfo=timezone.utc)
        self.universe_pass = UniverseDecision(True, (), FeedAssessment(True, True, False, ()))

    def security(self, status, reasons=()):
        return SecurityDecision(status, reasons, None, self.now, "m3.2")

    def test_only_passing_universe_and_security_allows_entry(self):
        result = decide(self.universe_pass, self.security(SecurityStatus.PASS), self.now)
        self.assertTrue(result.allowed)
        self.assertEqual((), result.reasons)
        self.assertEqual(self.now, result.evaluated_at)

    def test_unknown_and_reject_security_always_block_entry(self):
        unknown = decide(self.universe_pass, self.security(SecurityStatus.UNKNOWN, ("PROVIDER_ERROR",)), self.now)
        rejected = decide(self.universe_pass, self.security(SecurityStatus.REJECT, ("NOT_TRADABLE",)), self.now)
        self.assertEqual(("SECURITY:UNKNOWN", "SECURITY:PROVIDER_ERROR"), unknown.reasons)
        self.assertEqual(("SECURITY:REJECT", "SECURITY:NOT_TRADABLE"), rejected.reasons)
        self.assertFalse(unknown.allowed)
        self.assertFalse(rejected.allowed)

    def test_universe_failure_is_preserved_in_audit_reasons(self):
        universe = UniverseDecision(False, ("FEED_NOT_READY",), FeedAssessment(True, False, True, ()))
        result = decide(universe, self.security(SecurityStatus.PASS), self.now)
        self.assertFalse(result.allowed)
        self.assertEqual(("UNIVERSE:FEED_NOT_READY",), result.reasons)


if __name__ == "__main__":
    unittest.main()
