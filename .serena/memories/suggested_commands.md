# Suggested Windows commands

Run from the project root in PowerShell. Prefix noisy commands with `rtk` as defined in `RTK.md`.

- Verify RTK: `rtk --version` and `rtk gain`
- Sync project environment: `rtk uv sync`
- Start safely: `rtk uv run python -m meme_ai_trader`
- Run suite: `rtk uv run python -m unittest discover -s tests -v`
- PostgreSQL integration test needs `PGPASSWORD` supplied locally; never place its value in chat, Git, or command history.
- Exercise invalid mode: `$env:MEME_AI_MODE='live_auto'; rtk uv run python -m meme_ai_trader; Remove-Item Env:MEME_AI_MODE`
- Inspect concise Git state: `rtk git status --short --branch`
- Check patch whitespace: `rtk git diff --check` (or `rtk git diff --cached --check` after staging)
- Stage explicit reviewed paths, then commit; do not default to `git add .`.
- Push task branch: `rtk git push -u origin <branch>`