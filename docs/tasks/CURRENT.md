# M7.3 — Label TP/SL/no-route

Status: SELESAI pada 2026-09-16.

- Label outcome historis membedakan TP, SL, timeout, route unavailable, dan data kurang; tidak menganggap route sebagai fill.
- Tes: `uv run python -m unittest tests.test_labels tests.test_no_execution` — 3/3 lulus.

Berikutnya: M8.1 freeze experiment.
