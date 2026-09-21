import json
import unittest
from urllib.error import URLError

from meme_ai_trader.adapters.goplus import GoPlusClient, GoPlusError, GoPlusRateLimit
from meme_ai_trader.adapters.solana_rpc import SolanaRPCClient, SolanaRPCError, SolanaRPCRateLimit
from meme_ai_trader.adapters.telegram_client import TelegramClient, TelegramError, TelegramRateLimit


class Response:
    def __init__(self, payload, status=200):
        self.payload, self.status = payload, status

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def read(self):
        return self.payload if isinstance(self.payload, bytes) else json.dumps(self.payload).encode()


class ProviderClientTests(unittest.TestCase):
    def test_solana_success_is_read_only(self):
        seen = []

        def opener(request, timeout):
            seen.append((request.get_method(), timeout, json.loads(request.data)))
            return Response({"jsonrpc": "2.0", "result": {"value": {"lamports": 1}}})

        result = SolanaRPCClient("https://rpc.test", opener).account_info("mint")
        self.assertEqual({"value": {"lamports": 1}}, result)
        self.assertEqual("POST", seen[0][0])
        self.assertEqual("getAccountInfo", seen[0][2]["method"])

    def test_solana_rate_limit_timeout_bad_and_missing(self):
        with self.assertRaises(SolanaRPCRateLimit):
            SolanaRPCClient("https://rpc.test", lambda *_, **__: Response({}, 429)).request("getSlot")
        with self.assertRaises(SolanaRPCError):
            SolanaRPCClient("https://rpc.test", lambda *_, **__: (_ for _ in ()).throw(TimeoutError())).request("getSlot")
        with self.assertRaises(SolanaRPCError):
            SolanaRPCClient("https://rpc.test", lambda *_, **__: Response(b"bad")).request("getSlot")
        with self.assertRaises(SolanaRPCError):
            SolanaRPCClient("https://rpc.test", lambda *_, **__: Response({"jsonrpc": "2.0", "result": None})).request("getSlot")

    def test_goplus_success_and_missing(self):
        result = GoPlusClient("key", "https://goplus.test", lambda *_, **__: Response({"code": 1, "result": {"is_in_dex": "1"}})).token_security("mint")
        self.assertEqual("1", result["is_in_dex"])
        with self.assertRaises(GoPlusError):
            GoPlusClient("key", "https://goplus.test", lambda *_, **__: Response({"code": 1, "result": {}})).token_security("mint")

    def test_goplus_rate_limit_bad_and_timeout(self):
        with self.assertRaises(GoPlusRateLimit):
            GoPlusClient("key", "https://goplus.test", lambda *_, **__: Response({}, 429)).token_security("mint")
        with self.assertRaises(GoPlusError):
            GoPlusClient("key", "https://goplus.test", lambda *_, **__: Response(b"bad")).token_security("mint")
        with self.assertRaises(GoPlusError):
            GoPlusClient("key", "https://goplus.test", lambda *_, **__: (_ for _ in ()).throw(URLError("timeout"))).token_security("mint")

    def test_telegram_allowlist_success_and_failure(self):
        seen = []

        def opener(request, timeout):
            seen.append(json.loads(request.data))
            return Response({"ok": True, "result": {"message_id": 1}})

        client = TelegramClient("token", "123", opener)
        self.assertEqual(1, client.send_test("123", "TEST diagnostic")["message_id"])
        self.assertEqual("123", seen[0]["chat_id"])
        with self.assertRaises(TelegramError):
            client.send_message("999", "TEST outside")
        with self.assertRaises(ValueError):
            client.send_test("123", "diagnostic")

    def test_telegram_rate_limit_bad_and_timeout(self):
        with self.assertRaises(TelegramRateLimit):
            TelegramClient("token", "123", lambda *_, **__: Response({}, 429)).send_test("123", "TEST rate")
        with self.assertRaises(TelegramError):
            TelegramClient("token", "123", lambda *_, **__: Response(b"bad")).send_test("123", "TEST bad")
        with self.assertRaises(TelegramError):
            TelegramClient("token", "123", lambda *_, **__: (_ for _ in ()).throw(TimeoutError())).send_test("123", "TEST timeout")


if __name__ == "__main__":
    unittest.main()
