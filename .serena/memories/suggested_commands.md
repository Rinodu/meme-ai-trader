# Suggested Windows commands

Run from the project root in PowerShell.

- Sync project environment: `uv sync`
- Start safely: `uv run python -m meme_ai_trader`
- Run suite: `uv run python -m unittest discover -s tests -v`
- PostgreSQL integration test needs `PGPASSWORD` supplied locally; never place its value in chat, Git, or command history.
- Exercise invalid mode: `$env:MEME_AI_MODE='live_auto'; uv run python -m meme_ai_trader; Remove-Item Env:MEME_AI_MODE`
- Inspect concise Git state: `git status --short --branch`
- Check patch whitespace: `git diff --check` (or `git diff --cached --check` after staging)
- Stage explicit reviewed paths, then commit; do not default to `git add .`.
- Push task branch: `git push -u origin <branch>`