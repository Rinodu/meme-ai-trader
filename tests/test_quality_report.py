import unittest
from datetime import datetime, timezone
from decimal import Decimal

from meme_ai_trader.quality_report import QualityStatus, build_quality_report


START = "2026-01-01T00:00:00Z"
END = "2026-01-31T23:59:59Z"
GENERATED = datetime(2026, 2, 1, tzinfo=timezone.utc)


def outcomes(size, status="MATCH"):
    return [
        {"signal_id": f"s-{index}", "status": status, "timestamp": f"2026-01-{(index % 30) + 1:02d}T00:00:00Z"}
        for index in range(size)
    ]


class QualityReportTests(unittest.TestCase):
    def test_valid_report_with_thirty_samples(self):
        records = outcomes(29) + [{"signal_id": "s-29", "status": "DEVIATION", "timestamp": "2026-01-30T00:00:00Z"}]
        report = build_quality_report("r1", START, END, records, 30, generated_at=GENERATED)
        self.assertEqual(QualityStatus.VALID, report.status)
        self.assertEqual(Decimal("0.033333"), report.deviation_ratio)

    def test_small_sample_is_inconclusive(self):
        report = build_quality_report("r2", START, END, outcomes(2), 2, generated_at=GENERATED)
        self.assertEqual(QualityStatus.INCONCLUSIVE, report.status)

    def test_no_valid_outcome_is_insufficient(self):
        report = build_quality_report("r3", START, END, outcomes(2, "INSUFFICIENT_DATA"), 2, generated_at=GENERATED)
        self.assertEqual(QualityStatus.INSUFFICIENT_DATA, report.status)
        self.assertIsNone(report.deviation_ratio)

    def test_unknown_outcome_fails_validation(self):
        with self.assertRaises(ValueError):
            build_quality_report("r4", START, END, outcomes(1, "UNKNOWN"), 1)

    def test_deviation_ratio_is_deterministic(self):
        records = outcomes(28) + outcomes(2, "DEVIATION")
        records[-2]["signal_id"] = "s-deviation-1"
        records[-1]["signal_id"] = "s-deviation-2"
        report = build_quality_report("r5", START, END, records, 30, generated_at=GENERATED)
        self.assertEqual(Decimal("0.066667"), report.deviation_ratio)

    def test_data_coverage_uses_all_signals(self):
        report = build_quality_report("r6", START, END, outcomes(2), 4, generated_at=GENERATED)
        self.assertEqual(Decimal("0.500000"), report.data_coverage)

    def test_uncalibrated_probability_is_hidden(self):
        report = build_quality_report(
            "r7", START, END, outcomes(30), 30,
            probability_data={"values": ["0.8"], "out_of_sample": False, "calibrated": False, "score": "high"},
            generated_at=GENERATED,
        )
        self.assertFalse(report.probability_available)
        self.assertEqual("UNAVAILABLE", report.calibration_summary["status"])
        self.assertIn("score", report.calibration_summary)

    def test_missing_metrics_are_null(self):
        report = build_quality_report("r8", START, END, outcomes(30), 30, generated_at=GENERATED)
        self.assertIsNone(report.drawdown)
        self.assertIsNone(report.expectancy)

    def test_duplicate_signal_id_fails_validation(self):
        records = outcomes(2)
        records[1]["signal_id"] = records[0]["signal_id"]
        with self.assertRaises(ValueError):
            build_quality_report("r9", START, END, records, 2)

    def test_invalid_timestamp_fails_validation(self):
        records = outcomes(1)
        records[0]["timestamp"] = "broken"
        with self.assertRaises(ValueError):
            build_quality_report("r10", START, END, records, 1)
