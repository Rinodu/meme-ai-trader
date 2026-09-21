import unittest
from datetime import datetime, timezone

from meme_ai_trader.config import Settings
from meme_ai_trader.operational_gate import audit_signal_only


NOW = datetime(2026, 9, 21, tzinfo=timezone.utc)


class OperationalGateTests(unittest.TestCase):
    def setUp(self):
        self.settings = Settings.from_env({"MEME_AI_MODE": "paper_signal"})

    def test_all_checks_pass(self):
        report = audit_signal_only(self.settings, True, True, NOW)
        self.assertEqual("PASS", report.status)
        self.assertEqual("PASS", report.checks["execution_boundary"])

    def test_data_failure_is_fail_closed(self):
        report = audit_signal_only(self.settings, False, True, NOW)
        self.assertEqual("FAIL", report.status)
        self.assertIn("DATA_CHECK_FAILED", report.reasons)

    def test_allowlist_failure_is_fail_closed(self):
        report = audit_signal_only(self.settings, True, False, NOW)
        self.assertEqual("FAIL", report.status)
        self.assertIn("ALLOWLIST_CHECK_FAILED", report.reasons)

    def test_safe_runtime_modes_are_accepted(self):
        for mode in ("collect_only", "replay", "paper_signal"):
            settings = Settings.from_env({"MEME_AI_MODE": mode})
            self.assertEqual("PASS", audit_signal_only(settings, True, True, NOW).status)


if __name__ == "__main__":
    unittest.main()
