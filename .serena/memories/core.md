# Project core

- Solana meme-token trading system, built milestone-by-milestone; Telegram first.
- Safety invariant: default `collect_only`; no setup/startup side effect may activate live trading. LLM never accesses signer/private keys.
- Source map: `meme_ai_trader/config.py` owns environment validation; `meme_ai_trader/__main__.py` is the CLI; `meme_ai_trader/database/migrations/` owns PostgreSQL schema/identity indexes; `meme_ai_trader/database/raw_events.py` owns migration execution, dedup insert, UTC validation, and point-in-time reads.
- Tests: `tests/test_config.py` covers config; `tests/test_raw_events_integration.py` covers PostgreSQL migration, round-trip, dedup, and late-event reads.
- Control docs: `AGENTS.md` working rules; `AI_CONTEXT.md` current handoff; `docs/tasks/CURRENT.md` sole active task; `PROGRESS.md` official checklist; `FEATURES.md` stable behavior contracts; `ROADMAP.md` dependency order.
- One subtask per user request. Preserve old behavior; discuss behavior removal/change before implementation. Never invent provider access, credentials, runtime evidence, or test results.
- Read runtime/dependency details in `mem:tech_stack`; Windows commands in `mem:suggested_commands`; project coding rules in `mem:conventions`; completion gates in `mem:task_completion`.