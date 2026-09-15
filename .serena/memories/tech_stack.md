# Tech stack

- Python >=3.11; verified development runtimes include CPython 3.11 and 3.12 on Windows.
- Current runtime uses Python standard library only; package metadata in `pyproject.toml`.
- Config is an immutable dataclass loaded from environment variables. Current supported mode: `collect_only` only.
- Planned stack (not proof of installation): PostgreSQL; Redis only if justified; Birdeye, GoPlus, Solana RPC, Jupiter; Telegram; optional LLM later.
- Docker/WSL are not project prerequisites. Use a local Windows virtual environment; do not upgrade global Python casually.
- GitHub remote is private; task work uses dedicated branches and never auto-merges to main.