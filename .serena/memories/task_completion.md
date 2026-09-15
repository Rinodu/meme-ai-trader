# Task completion

Before marking a coding subtask complete:

1. Run `uv run python -m unittest discover -s tests -v`; supply PostgreSQL credentials privately when database integration is in scope.
2. For config/startup changes, run the CLI and at least one expected rejection path; verify no secret output.
3. Run Serena diagnostics, `git diff --check`, inspect the scoped diff, and verify `git status --short --branch` contains no unrelated/user changes. Record tool-only diagnostic limitations honestly.
4. Update `docs/tasks/CURRENT.md` and `AI_CONTEXT.md`; update `FEATURES.md`, `ROADMAP.md`, `CHANGELOG.md`, and `PROGRESS.md` only when their status/evidence changed.
5. Mark `PROGRESS.md` complete only with acceptance criteria and test evidence; keep milestone gate separate.
6. Stage explicit paths, run `git diff --cached --check`, commit, push the task branch, and report actual SHA/push status. Never auto-merge or activate live trading.