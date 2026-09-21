# M7.1 — Time replay

Status: SELESAI pada 2026-09-16.

- Replay memakai urutan availability `received_at`, termasuk input out-of-order, tanpa future-data leakage.
- Tes: `uv run python -m unittest tests.test_replay tests.test_quant tests.test_strategy tests.test_no_execution` — 10/10 lulus.

Berikutnya: M7.2 cost model simulator.
