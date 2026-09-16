import unittest
from decimal import Decimal

from meme_ai_trader.reporting import ReportStatus, report


class ReportTests(unittest.TestCase):
    def test_report_is_inconclusive_and_measures_drawdown(self):
        result = report([Decimal("2"), Decimal("-3"), Decimal("1")])
        self.assertEqual(Decimal("0"), result.expectancy)
        self.assertEqual(Decimal("1"), result.profit_factor)
        self.assertEqual(Decimal("3"), result.max_drawdown)
        self.assertEqual(ReportStatus.INCONCLUSIVE, result.status)
