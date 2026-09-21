import unittest
from datetime import datetime, timezone

from meme_ai_trader.recovery import RecoveryAction, decide_recovery


NOW = datetime(2026, 9, 21, tzinfo=timezone.utc)


class RecoveryTests(unittest.TestCase):
    def test_all_ok_requires_no_action(self):
        self.assertEqual(RecoveryAction.NO_ACTION, decide_recovery("i", "OK", "OK", True, 0, NOW).action)

    def test_stale_data_pauses_entries(self):
        result = decide_recovery("i", "STALE", "OK", True, 0, NOW)
        self.assertEqual(RecoveryAction.PAUSE_ENTRIES, result.action)
        self.assertIn("DATA_STALE", result.reasons)

    def test_provider_error_pauses_entries(self):
        self.assertEqual(RecoveryAction.PAUSE_ENTRIES, decide_recovery("i", "OK", "ERROR", True, 1, NOW).action)

    def test_unknown_state_escalates(self):
        result = decide_recovery("i", "OK", "OK", False, 0, NOW)
        self.assertEqual(RecoveryAction.ESCALATE, result.action)

    def test_invalid_input_fails_closed(self):
        with self.assertRaises(ValueError):
            decide_recovery("", "OK", "OK", True, 0, NOW)


if __name__ == "__main__":
    unittest.main()
