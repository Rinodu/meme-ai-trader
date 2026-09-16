# M4.3 — Replay deterministik

Status: SELESAI pada 2026-09-16.

- Replay mengurutkan event berdasarkan `received_at`, membangun fitur point-in-time, dan menghasilkan keputusan sama untuk input/policy sama.
- Tes: `uv run python -m unittest tests.test_replay tests.test_strategy tests.test_quant tests.test_no_execution` — 10/10 lulus.

Berikutnya: M5.1 sizing/exposure.
