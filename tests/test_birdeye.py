import json
import unittest
from datetime import datetime, timezone
from decimal import Decimal

from meme_ai_trader.adapters.birdeye import BirdeyeClient, BirdeyeError, raw_event


class _Response:
    status = 200

    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self):
        return json.dumps(self.payload).encode()


class BirdeyeTests(unittest.TestCase):
    def test_client_uses_read_only_solana_request(self):
        requests = []

        def opener(request, timeout):
            requests.append((request, timeout))
            return _Response({"success": True, "data": {"price": 0}})

        self.assertEqual({"price": 0}, BirdeyeClient("secret", opener).token_overview("mint address"))
        request, timeout = requests[0]
        self.assertEqual("GET", request.get_method())
        self.assertEqual("solana", request.get_header("X-chain"))
        self.assertEqual("secret", request.get_header("X-api-key"))
        self.assertEqual(10, timeout)
        self.assertIn("address=mint+address", request.full_url)

    def test_invalid_provider_response_is_safe(self):
        client = BirdeyeClient("secret", lambda *_, **__: _Response({"success": False, "message": "bad key"}))
        with self.assertRaisesRegex(BirdeyeError, "unsuccessful") as error:
            client.token_overview("mint")
        self.assertNotIn("secret", str(error.exception))

    def test_snapshot_preserves_zero_and_marks_missing_fields(self):
        snapshot = {"price": 0, "mc": None, "fdv": "12.5", "liquidity": 0,
                    "v1hUSD": 0, "buy1h": 0, "sell1h": 1, "priceChange1hPercent": -2}
        event = raw_event("mint", snapshot, datetime(2026, 9, 15, tzinfo=timezone.utc))
        self.assertEqual(Decimal("0"), event["price"])
        self.assertIsNone(event["market_cap"])
        self.assertEqual(Decimal("-2"), event["price_change_1h"])
        self.assertEqual(["market_cap"], event["missing_fields"])
        self.assertEqual(snapshot, event["raw_payload"])


if __name__ == "__main__":
    unittest.main()
