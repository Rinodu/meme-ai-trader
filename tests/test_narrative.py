import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from meme_ai_trader.narrative import (
    NarrativeConfig,
    NarrativeService,
    NarrativeStatus,
    ProviderNarrative,
    SocialEvidence,
    SocialStatus,
)
from meme_ai_trader.strategy import Signal


MINT = "So11111111111111111111111111111111111111112"
NOW = datetime(2026, 9, 21, 10, tzinfo=timezone.utc)


def evidence(source_id="fixture-1", status=SocialStatus.AVAILABLE):
    return SocialEvidence(MINT, "fixture", source_id, NOW, NOW, "fixture text", status)


class FakeProvider:
    def __init__(self, result=None, error=None):
        self.calls = 0
        self.result = result or ProviderNarrative("fixture narrative", evidence_refs=("fixture-1",), cost_idr=Decimal("10"))
        self.error = error

    def estimate_cost_idr(self, _evidence):
        return Decimal("10")

    def complete(self, _evidence, _timeout):
        self.calls += 1
        if self.error:
            raise self.error
        return ProviderNarrative(self.result.summary, self.result.catalyst_status, (_evidence.source_id,), self.result.uncertainties, self.result.cost_idr)


class NarrativeTests(unittest.TestCase):
    def test_no_provider_and_fixture_are_not_live(self):
        result = NarrativeService().analyze(evidence(), NOW)
        self.assertEqual(NarrativeStatus.DISABLED, result.status)
        self.assertIn("LLM_DISABLED", result.reason)

    def test_budget_zero_is_hard_stop(self):
        provider = FakeProvider()
        result = NarrativeService(NarrativeConfig(enabled=True), provider).analyze(evidence(), NOW)
        self.assertEqual(NarrativeStatus.DISABLED, result.status)
        self.assertEqual(0, provider.calls)

    def test_cache_hit_and_expiry(self):
        provider = FakeProvider()
        config = NarrativeConfig(enabled=True, monthly_budget_idr=Decimal("100"), max_calls_per_month=10, cache_ttl_seconds=10)
        service = NarrativeService(config, provider)
        first = service.analyze(evidence(), NOW)
        cached = service.analyze(evidence(), NOW + timedelta(seconds=1))
        self.assertEqual(NarrativeStatus.AVAILABLE, first.status)
        self.assertEqual(NarrativeStatus.CACHE_HIT, cached.status)
        self.assertEqual(1, provider.calls)
        refreshed = service.analyze(evidence("fixture-2"), NOW + timedelta(seconds=11))
        self.assertEqual(NarrativeStatus.AVAILABLE, refreshed.status)
        self.assertEqual(2, provider.calls)

    def test_timeout_and_provider_failure_fallback(self):
        provider = FakeProvider(error=TimeoutError())
        config = NarrativeConfig(enabled=True, monthly_budget_idr=Decimal("100"), max_calls_per_month=10, max_retries=1)
        result = NarrativeService(config, provider).analyze(evidence(), NOW)
        self.assertEqual(NarrativeStatus.UNAVAILABLE, result.status)
        self.assertEqual(2, provider.calls)

    def test_unknown_cost_and_budget_cap_fail_closed(self):
        class UnknownCost(FakeProvider):
            def estimate_cost_idr(self, _evidence):
                return None
        provider = UnknownCost()
        result = NarrativeService(NarrativeConfig(enabled=True, monthly_budget_idr=Decimal("100"), max_calls_per_month=10), provider).analyze(evidence(), NOW)
        self.assertEqual(0, provider.calls)
        self.assertIn("COST_UNKNOWN", result.reason)

    def test_budget_exhaustion_blocks_next_call(self):
        provider = FakeProvider()
        config = NarrativeConfig(enabled=True, monthly_budget_idr=Decimal("10"), max_calls_per_month=10)
        service = NarrativeService(config, provider)
        self.assertEqual(NarrativeStatus.AVAILABLE, service.analyze(evidence("fixture-1"), NOW).status)
        blocked = service.analyze(evidence("fixture-2"), NOW)
        self.assertEqual(NarrativeStatus.UNAVAILABLE, blocked.status)
        self.assertIn("BUDGET_EXHAUSTED", blocked.reason)

    def test_input_bound_is_validated(self):
        with self.assertRaises(ValueError):
            SocialEvidence(MINT, "fixture", "long", NOW, NOW, "x" * 4001)

    def test_social_data_status_and_duplicate(self):
        service = NarrativeService()
        self.assertIn("DATA_STALE", service.analyze(evidence(status=SocialStatus.STALE), NOW).reason)
        provider = FakeProvider()
        service = NarrativeService(NarrativeConfig(enabled=False), provider)
        service.analyze(evidence(), NOW)
        duplicate = service.analyze(evidence(), NOW)
        self.assertEqual("DUPLICATE", duplicate.reason)

    def test_fallback_does_not_change_signal(self):
        signal = Signal(True, None, NOW + timedelta(minutes=5))
        result = NarrativeService().analyze(evidence(), NOW)
        self.assertFalse(result.narrative_summary)
        self.assertTrue(signal.eligible)

    def test_output_never_claims_probability(self):
        provider = FakeProvider()
        config = NarrativeConfig(enabled=True, monthly_budget_idr=Decimal("100"), max_calls_per_month=10)
        result = NarrativeService(config, provider).analyze(evidence(), NOW)
        self.assertFalse(result.as_dict()["probability_available"])


if __name__ == "__main__":
    unittest.main()
