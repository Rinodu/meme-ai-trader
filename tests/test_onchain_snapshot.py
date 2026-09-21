import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import meme_ai_trader.onchain_snapshot as snapshot_module
from meme_ai_trader.onchain_snapshot import SnapshotStatus, assess_snapshot


NOW = datetime(2026, 9, 21, 12, 0, tzinfo=timezone.utc)
MINT = "11111111111111111111111111111111"


def snapshot(**overrides):
    value = {
        "schema_version": 1,
        "chain": "solana",
        "network": "mainnet-beta",
        "mint_address": MINT,
        "observed_at": NOW - timedelta(seconds=30),
        "source": "solana-rpc",
        "rpc_slot": 123,
        "commitment": "confirmed",
        "token_supply": "1000000",
        "decimals": 6,
        "mint_authority": None,
        "freeze_authority": None,
        "holder_count": 100,
        "top_holder_ratio": Decimal("0.2"),
        "liquidity": Decimal("1000"),
        "liquidity_locked": True,
    }
    value.update(overrides)
    return value


class OnChainSnapshotTests(unittest.TestCase):
    def test_fresh_complete_snapshot_is_accepted(self):
        result = assess_snapshot(snapshot(), NOW)
        self.assertEqual(SnapshotStatus.FRESH, result.data_status)
        self.assertTrue(result.allows_signal())

    def test_snapshot_over_120_seconds_is_stale(self):
        result = assess_snapshot(snapshot(observed_at=NOW - timedelta(seconds=121)), NOW)
        self.assertEqual(SnapshotStatus.STALE, result.data_status)
        self.assertFalse(result.allows_signal())

    def test_snapshot_age_limit_is_configurable(self):
        result = assess_snapshot(snapshot(observed_at=NOW - timedelta(seconds=31)), NOW, max_snapshot_age_seconds=30)
        self.assertEqual(SnapshotStatus.STALE, result.data_status)

    def test_future_timestamp_beyond_tolerance_is_invalid(self):
        result = assess_snapshot(snapshot(observed_at=NOW + timedelta(seconds=6)), NOW)
        self.assertEqual(SnapshotStatus.INVALID, result.data_status)

    def test_missing_snapshot_is_missing(self):
        result = assess_snapshot(None, NOW)
        self.assertEqual(SnapshotStatus.MISSING, result.data_status)
        self.assertFalse(result.allows_signal())

    def test_missing_required_field_is_invalid(self):
        value = snapshot()
        del value["source"]
        result = assess_snapshot(value, NOW)
        self.assertEqual(SnapshotStatus.INVALID, result.data_status)
        self.assertIn("source", result.missing_fields)

    def test_missing_optional_field_is_partial(self):
        value = snapshot()
        del value["holder_count"]
        result = assess_snapshot(value, NOW)
        self.assertEqual(SnapshotStatus.PARTIAL, result.data_status)
        self.assertIn("holder_count", result.missing_fields)
        self.assertTrue(result.allows_signal())

    def test_processed_commitment_is_rejected(self):
        result = assess_snapshot(snapshot(commitment="processed"), NOW)
        self.assertEqual(SnapshotStatus.INVALID, result.data_status)

    def test_confirmed_and_finalized_are_accepted(self):
        self.assertEqual(SnapshotStatus.FRESH, assess_snapshot(snapshot(commitment="confirmed"), NOW).data_status)
        self.assertEqual(SnapshotStatus.FRESH, assess_snapshot(snapshot(commitment="finalized"), NOW).data_status)

    def test_invalid_mint_is_rejected(self):
        result = assess_snapshot(snapshot(mint_address="not-a-mint"), NOW)
        self.assertEqual(SnapshotStatus.INVALID, result.data_status)

    def test_network_or_mint_mismatch_is_rejected(self):
        self.assertEqual(SnapshotStatus.INVALID, assess_snapshot(snapshot(), NOW, expected_network="devnet").data_status)
        self.assertEqual(SnapshotStatus.INVALID, assess_snapshot(snapshot(), NOW, expected_mint_address="2" * 32).data_status)

    def test_negative_values_are_rejected(self):
        self.assertEqual(SnapshotStatus.INVALID, assess_snapshot(snapshot(token_supply=-1), NOW).data_status)
        self.assertEqual(SnapshotStatus.INVALID, assess_snapshot(snapshot(liquidity=-1), NOW).data_status)

    def test_stale_missing_invalid_never_allow_signal(self):
        cases = (
            assess_snapshot(snapshot(observed_at=NOW - timedelta(seconds=121)), NOW),
            assess_snapshot(None, NOW),
            assess_snapshot(snapshot(commitment="processed"), NOW),
        )
        self.assertTrue(all(not case.allows_signal() for case in cases))

    def test_missing_values_are_not_converted_to_zero(self):
        value = snapshot()
        del value["liquidity"]
        result = assess_snapshot(value, NOW)
        self.assertIsNone(result.liquidity)
        self.assertNotEqual(Decimal("0"), result.liquidity)

    def test_snapshot_output_contains_schema_fields(self):
        result = assess_snapshot(snapshot(), NOW)
        output = result.as_dict()
        for field in ("schema_version", "chain", "network", "mint_address", "observed_at", "source", "rpc_slot", "commitment", "data_status", "missing_fields", "warnings"):
            self.assertIn(field, output)

    def test_snapshot_module_has_no_execution_api(self):
        for forbidden in ("sign", "submit", "private_key"):
            self.assertFalse(any(forbidden in name.lower() for name in dir(snapshot_module)))
