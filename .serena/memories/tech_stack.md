# Tech stack

- Python >=3.11; project-local runtime pinned to CPython 3.12 with `uv`.
- Runtime dependencies are locked in `uv.lock`; M2.1 uses Psycopg 3.3.5 with binary extras.
- PostgreSQL 18.6 is installed locally on Windows as service `postgresql-x64-18`, listening on localhost:5432.
- Config is an immutable dataclass loaded from environment variables. Current supported mode: `collect_only` only.
- Redis only if justified. Planned integrations (not proof of access): Birdeye, GoPlus, Solana RPC, Jupiter, Telegram, and optional LLM later.
- Docker/WSL are not project prerequisites. Do not upgrade global Python casually.
- GitHub remote is private; task work uses dedicated branches and never auto-merges to main.