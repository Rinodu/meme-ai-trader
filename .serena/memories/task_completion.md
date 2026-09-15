# Task completion

Before marking a coding subtask complete:

1. Run `py -m unittest discover -s tests -v`; run Python 3.11 explicitly when compatibility changed.
2. For config/startup changes, run `py -m meme_ai_trader` and at least one expected rejection path; verify no secret output.
3. Run `git diff --check`, inspect the scoped diff, and verify `git status --short --branch` contains no unrelated/user changes.
4. Update `docs/tasks/CURRENT.md` and `AI_CONTEXT.md`; update `FEATURES.md`, `ROADMAP.md`, `CHANGELOG.md`, and `PROGRESS.md` only when their status/evidence changed.
5. Mark `PROGRESS.md` complete only with acceptance criteria and test evidence; keep milestone gate separate.
6. Stage explicit paths, run `git diff --cached --check`, commit, push the task branch, and report actual SHA/push status. Never auto-merge or activate live trading.