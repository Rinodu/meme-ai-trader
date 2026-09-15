# Suggested Windows commands

Run from the project root in PowerShell.

- Start safely: `py -m meme_ai_trader`
- Run focused/full current suite: `py -m unittest discover -s tests -v`
- Verify minimum runtime: `py -V:Astral/CPython3.11.16 -m unittest discover -s tests -v`
- Exercise invalid mode: `$env:MEME_AI_MODE='live_auto'; py -m meme_ai_trader; Remove-Item Env:MEME_AI_MODE`
- Inspect concise Git state: `git status --short --branch`
- Check patch whitespace: `git diff --check` (or `git diff --cached --check` after staging)
- Stage explicit reviewed paths, then commit; do not default to `git add .`.
- Push task branch: `git push -u origin <branch>`