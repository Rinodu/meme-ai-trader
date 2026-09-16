# M5.3 — Exit/kill switch simulator

Status: SELESAI pada 2026-09-16.

- Mode pause/reduce memblokir entry baru; pengendalian legacy hanya simulator dan guard Signal Bot tetap meniadakan signing/execution.
- Tes: `uv run python -m unittest tests.test_controls tests.test_no_execution` — 3/3 lulus.

Berikutnya: M6.1 intent/attempt simulator.
