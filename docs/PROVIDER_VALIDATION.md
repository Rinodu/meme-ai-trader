# Provider validation matrix

Status: configuration and estimates only. No production credential is stored or
enabled. `40/40` and milestone status are unchanged; fixture tests are not live
provider validation.

## Implemented endpoint inventory

| Provider/endpoint | Code status | Normal call model | Required data/freshness | Failure behavior |
| --- | --- | --- | --- | --- |
| Birdeye `GET /defi/token_overview` | Implemented in `adapters/birdeye.py` | 1 call per candidate per scan; client timeout 10s | price, liquidity, volume/trades fields as available; repository assesses freshness | error/invalid payload rejects collection; partial fields remain explicit |
| Solana RPC `getAccountInfo`/`getTokenSupply` | Client implemented; not live-tested | 0 actual calls | M12.1 snapshot schema, commitment confirmed/finalized, max age 120s | timeout/429/error/missing result raises; signal path must fail closed |
| GoPlus Solana Token Security API | Client implemented; not live-tested | 0 actual calls | security result must be complete/fresh before gate | timeout/429/error/missing result raises; UNKNOWN/reject |
| Telegram Bot API `sendMessage` | Allowlist-only client implemented; not live-tested | 0 actual calls | private allowlisted chat only; diagnostic must be TEST-labelled | non-allowlisted chat rejected before network call; errors raise |

## Usage model (estimate, not measurement)

Let `C` be candidates per scan, `S` scans/day, and `D=30` days. The only current
provider call is Birdeye: `calls/day = C*S`, `calls/month = 30*C*S`.

| Profile | C | S/day | Birdeye calls/day | Birdeye calls/month |
| --- | ---: | ---: | ---: | ---: |
| Slow | 10 | 24 | 240 | 7,200 |
| Moderate | 25 | 96 | 2,400 | 72,000 |
| Intensive | 50 | 288 | 14,400 | 432,000 |

RPC/GoPlus/Telegram clients exist tetapi belum live-tested atau terhubung ke
runtime end-to-end. Dengan `R` RPC calls dan `G` GoPlus calls per kandidat,
gunakan `30*C*S*R` dan `30*C*S*G`; ukur respons dan quota header aktual, jangan
menganggap paket akun mencakup endpoint tersebut.

## Official limit comparison

- Birdeye's current pricing page lists Standard as free; Lite is $39/month with
  2.5M CUs/month and 15 rps, Starter $99/8M CUs/15 rps, Premium $199/20M CUs/50
  rps. Free Standard quota must be verified in the account before use.
- Solana public RPC is rate-limited and explicitly not intended for production;
  published limits include 100 requests/10 seconds/IP and 40 requests/10 seconds
  per single RPC. A dedicated RPC is required after load testing.
- GoPlus documents a free tier of 150k CU/month, 30k/day, and 150/min; batch is
  not enabled on that tier. Actual endpoint coverage for this bot remains untested.
- Telegram Bot API is HTTPS. Private-chat sending is free under normal limits;
  roughly 1 message/second per chat and about 30 messages/second broadcast limit.

## Environment-only configuration

Konfigurasi dibaca dari environment proses oleh
`meme_ai_trader.provider_config.ProviderConfig`. Aplikasi tidak otomatis memuat
file `.env`; jangan mengandalkan file tersebut tanpa mengekspor nilainya ke
environment. Jangan tempel nilai rahasia ke chat atau commit ke Git.

```dotenv
MEME_AI_BIRDEYE_ENABLED=false
BIRDEYE_API_KEY=
MEME_AI_SOLANA_RPC_ENABLED=false
SOLANA_RPC_URL=https://api.mainnet.solana.com
MEME_AI_GOPLUS_ENABLED=false
GOPLUS_API_KEY=
GOPLUS_TOKEN_SECURITY_URL=https://api.gopluslabs.io/api/v1/solana/token_security
MEME_AI_TELEGRAM_ENABLED=false
TELEGRAM_BOT_TOKEN=
TELEGRAM_ALLOWED_CHAT_ID=
MEME_AI_LLM_ENABLED=false
MEME_AI_LLM_MONTHLY_BUDGET_IDR=0
```

The parser rejects enabled providers without credentials/allowlist and rejects any
LLM activation or non-zero budget. This file is an example only; it is not a smoke
test and does not prove endpoint availability.

Windows setup: set Process environment variables in PowerShell
(`$env:NAME = 'value'`). Obtain Birdeye/GoPlus keys from their official
developer consoles, a Solana RPC URL from the selected RPC provider, and the
Telegram bot token/chat ID from BotFather and the private chat. Do not paste any
value into chat or commit the file.

## Gate for a later smoke test

After credentials are installed locally, run `uv run python scripts/provider_smoke.py
--mint <MINT> --max-calls 1`; add `--telegram-test` only after the private chat ID
is allowlisted. Run only read-only `collect_only` and `paper_signal` probes with an
explicit call cap. Record latency, HTTP errors,
freshness, quota headers, and rejection reasons. Telegram's first message must be
`TEST` to the configured private allowlist chat. Do not emit a trade signal until
the provider response passes schema/freshness/security gates. Diagram alur,
setup bertahap, dan checklist pasca-perbaikan tersedia di
[`WORKFLOW_SETUP.md`](WORKFLOW_SETUP.md).
