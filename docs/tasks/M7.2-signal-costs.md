# M7.2 — Cost model simulator

Status: SELESAI pada 2026-09-16.

- Model biaya simulator menggunakan fee, slippage, dan impact basis point eksplisit tanpa default tersembunyi.
- Tes: `uv run python -m unittest tests.test_costs tests.test_no_execution` — 3/3 lulus.

Berikutnya: M7.3 label TP/SL/no-route.
