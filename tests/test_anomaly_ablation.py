import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from meme_ai_trader.anomaly_ablation import (
    AnomalyCode,
    AnomalyRules,
    CandidateObservation,
    evaluate_ablation,
    evaluate_candidate,
)
from meme_ai_trader.labels import Outcome
from meme_ai_trader.onchain_snapshot import SnapshotStatus, assess_snapshot
from meme_ai_trader.quality_report import QualityStatus


NOW = datetime(2026, 9, 21, 12, 0, tzinfo=timezone.utc)
MINT = "11111111111111111111111111111111"


def make_snapshot(**overrides):
    value = {
        "schema_version": 1, "chain": "solana", "network": "mainnet-beta", "mint_address": MINT,
        "observed_at": NOW - timedelta(seconds=30), "source": "solana-rpc", "rpc_slot": 123,
        "commitment": "confirmed", "token_supply": "1000000", "decimals": 6,
        "mint_authority": None, "freeze_authority": None, "holder_count": 100,
        "top_holder_ratio": Decimal("0.2"), "liquidity": Decimal("1000"), "liquidity_locked": True,
    }
    value.update(overrides)
    return assess_snapshot(value, NOW)


def candidate(name, snapshot=None, outcome=Outcome.TP_FIRST, eligible=True, cost="1"):
    return CandidateObservation(name, NOW, snapshot or make_snapshot(), eligible, outcome, Decimal(cost))


class AnomalyAblationTests(unittest.TestCase):
    def test_anomaly_detected_above_threshold(self):
        decision = evaluate_candidate(candidate("high", make_snapshot(top_holder_ratio=Decimal("0.8"))), AnomalyRules("test-v1", max_top_holder_ratio=Decimal("0.5")))
        self.assertFalse(decision.passed)
        self.assertIn(AnomalyCode.TOP_HOLDER_RATIO_HIGH, decision.anomaly_codes)

    def test_threshold_boundary_is_not_anomaly(self):
        decision = evaluate_candidate(candidate("edge", make_snapshot(top_holder_ratio=Decimal("0.5"))), AnomalyRules("test-v1", max_top_holder_ratio=Decimal("0.5")))
        self.assertTrue(decision.passed)

    def test_low_liquidity_anomaly_uses_parameterized_units(self):
        decision = evaluate_candidate(candidate("thin", make_snapshot(liquidity=Decimal("99"))), AnomalyRules("test-v1", min_liquidity=Decimal("100")))
        self.assertIn(AnomalyCode.LIQUIDITY_BELOW_THRESHOLD, decision.anomaly_codes)

    def test_missing_and_stale_are_data_not_anomaly(self):
        rules = AnomalyRules("test-v1", max_top_holder_ratio=Decimal("0.5"))
        partial = make_snapshot(top_holder_ratio=None)
        stale = make_snapshot(observed_at=NOW - timedelta(seconds=121))
        for value in (partial, stale):
            decision = evaluate_candidate(candidate("data", value), rules)
            self.assertFalse(decision.passed)
            self.assertEqual((), decision.anomaly_codes)
            self.assertIn("DATA_NOT_READY", decision.reasons)

    def test_baseline_and_filter_share_dataset_and_report_lost_outcome(self):
        rules = AnomalyRules("test-v1", max_top_holder_ratio=Decimal("0.5"), minimum_labeled=2)
        records = [candidate("ok-1"), candidate("bad-1", make_snapshot(top_holder_ratio=Decimal("0.9")), Outcome.SL_FIRST, cost="2"), candidate("ok-2", outcome=Outcome.TIMEOUT)]
        report = evaluate_ablation(records, rules, NOW)
        self.assertEqual(3, report.candidate_count)
        self.assertEqual(Decimal("1.000000"), report.coverage_baseline)
        self.assertEqual(Decimal("0.666667"), report.coverage_baseline_plus_filter)
        self.assertEqual(1, len(report.outcomes_lost_to_filter))
        self.assertEqual(QualityStatus.VALID, report.status)

    def test_no_data_leakage_from_future_snapshot(self):
        future = make_snapshot(observed_at=NOW + timedelta(seconds=1))
        record = candidate("future", future, Outcome.TP_FIRST)
        decision = evaluate_candidate(record, AnomalyRules("test-v1"))
        self.assertFalse(decision.passed)
        self.assertIn("DATA_LEAKAGE", decision.reasons)

    def test_coverage_and_costs_have_explicit_denominators(self):
        rules = AnomalyRules("test-v1", max_top_holder_ratio=Decimal("0.5"), minimum_labeled=1)
        report = evaluate_ablation([candidate("a", cost="2"), candidate("b", cost="3", eligible=False)], rules, NOW)
        self.assertEqual(Decimal("0.500000"), report.coverage_baseline)
        self.assertEqual(Decimal("2"), report.baseline.total_cost)
        self.assertEqual(Decimal("2"), report.baseline.average_cost)

    def test_insufficient_and_inconclusive_statuses(self):
        self.assertEqual(QualityStatus.INSUFFICIENT_DATA, evaluate_ablation([], AnomalyRules("test-v1"), NOW).status)
        report = evaluate_ablation([candidate("small")], AnomalyRules("test-v1"), NOW)
        self.assertEqual(QualityStatus.INCONCLUSIVE, report.status)

    def test_active_authority_and_unlocked_liquidity_codes(self):
        rules = AnomalyRules("test-v1", reject_active_authorities=True, require_liquidity_locked=True)
        decision = evaluate_candidate(candidate("risk", make_snapshot(mint_authority=MINT, freeze_authority=MINT, liquidity_locked=False)), rules)
        self.assertFalse(decision.passed)
        self.assertEqual(3, len(decision.anomaly_codes))

    def test_rules_require_nonempty_version_and_parameterized_thresholds(self):
        with self.assertRaises(ValueError):
            AnomalyRules("")
        rules = AnomalyRules("frozen-experiment-v1", min_liquidity=Decimal("100"))
        self.assertEqual("frozen-experiment-v1", rules.rule_version)
