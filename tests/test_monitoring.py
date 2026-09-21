import unittest
from datetime import datetime, timedelta, timezone

from meme_ai_trader.monitoring import monitor


NOW = datetime(2026, 9, 21, tzinfo=timezone.utc)


class MonitoringTests(unittest.TestCase):
    def test_healthy_snapshot(self):
        result = monitor("FRESH", True, True, True, NOW, NOW)
        self.assertEqual("HEALTHY", result.status)

    def test_stale_boundary_is_degraded(self):
        result = monitor("FRESH", True, True, True, NOW - timedelta(seconds=121), NOW)
        self.assertEqual("DEGRADED", result.status)
        self.assertIn("SNAPSHOT_STALE", result.alerts)

    def test_missing_or_invalid_is_critical(self):
        self.assertEqual("CRITICAL", monitor("MISSING", True, True, True, None, NOW).status)
        self.assertEqual("CRITICAL", monitor("INVALID", True, True, True, None, NOW).status)

    def test_provider_or_telegram_failure_is_degraded(self):
        result = monitor("FRESH", False, True, True, NOW, NOW)
        self.assertEqual("DEGRADED", result.status)
        self.assertIn("PROVIDER_UNHEALTHY", result.alerts)

    def test_failed_audit_and_future_time_are_critical(self):
        self.assertEqual("CRITICAL", monitor("FRESH", True, True, False, NOW, NOW).status)
        self.assertEqual("CRITICAL", monitor("FRESH", True, True, True, NOW + timedelta(seconds=1), NOW).status)

    def test_invalid_input_is_rejected(self):
        with self.assertRaises(ValueError):
            monitor("FRESH", True, True, True, NOW, NOW, 0)


if __name__ == "__main__":
    unittest.main()
