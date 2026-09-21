"""Bounded, opt-in read-only provider smoke test."""

import argparse
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from meme_ai_trader.adapters.birdeye import BirdeyeClient
from meme_ai_trader.adapters.goplus import GoPlusClient
from meme_ai_trader.adapters.solana_rpc import SolanaRPCClient
from meme_ai_trader.adapters.telegram_client import TelegramClient
from meme_ai_trader.provider_config import ProviderConfig


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mint", required=True)
    parser.add_argument("--max-calls", type=int, default=1)
    parser.add_argument("--telegram-test", action="store_true")
    args = parser.parse_args()
    if args.max_calls < 1:
        parser.error("--max-calls must be positive")
    config = ProviderConfig.from_env()
    calls = 0

    def call(label, function):
        nonlocal calls
        if calls >= args.max_calls:
            print(f"{label}: SKIPPED_CALL_CAP")
            return None
        started = time.perf_counter()
        try:
            value = function()
            print(f"{label}: PASS latency_ms={((time.perf_counter() - started) * 1000):.1f}")
            calls += 1
            return value
        except Exception as error:  # smoke report must continue to paper section
            print(f"{label}: FAIL reason={type(error).__name__}")
            calls += 1
            return None

    if config.birdeye_enabled:
        call("DATA_BIRDEYE", lambda: BirdeyeClient(config.birdeye_api_key).token_overview(args.mint))
    else:
        print("DATA_BIRDEYE: DISABLED")
    if config.solana_rpc_enabled:
        client = SolanaRPCClient(config.solana_rpc_url)
        call("DATA_SOLANA_RPC", lambda: client.account_info(args.mint))
    else:
        print("DATA_SOLANA_RPC: DISABLED")
    if config.goplus_enabled:
        client = GoPlusClient(config.goplus_api_key, config.goplus_token_security_url)
        call("DATA_GOPLUS", lambda: client.token_security(args.mint))
    else:
        print("DATA_GOPLUS: DISABLED")
    if args.telegram_test and config.telegram_enabled:
        client = TelegramClient(config.telegram_bot_token, config.telegram_allowed_chat_id)
        call("TELEGRAM_TEST", lambda: client.send_test(config.telegram_allowed_chat_id, "TEST provider smoke"))
    else:
        print("TELEGRAM_TEST: NOT_RUN")
    print("PAPER_SIGNAL: OBSERVATION_ONLY no live buy recommendation")
    print(f"generated_at={datetime.now(timezone.utc).isoformat()} calls={calls}/{args.max_calls}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
