# Conventions

- Documentation/user reports in Indonesian; code identifiers in English.
- Ponytail `full`: smallest correct change, reuse first, standard library/native features before dependencies, no speculative abstractions.
- Python: explicit type hints on public/config boundaries; immutable settings; clear `ConfigError` messages; secret fields excluded from representations/logs.
- Config environment variables use `MEME_AI_` prefix, except provider-standard secret names such as `BIRDEYE_API_KEY`.
- Tests use standard-library `unittest`; one focused test file is preferred over framework/scaffolding expansion.
- Default-deny at safety boundaries: unsupported modes and invalid flags fail startup; credentials are required only for enabled features.
- Never store `.env`, API keys, private keys, caches, or virtual environments in Git.
- Keep changes scoped to `docs/tasks/CURRENT.md`; archive completed task notes as `docs/tasks/Mx.y.md` when advancing.