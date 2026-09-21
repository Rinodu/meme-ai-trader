# M5.1 — Sizing/exposure simulator

Status: SELESAI pada 2026-09-16.

- Kalkulasi sizing hanya simulator: membatasi risk budget, position cap, portfolio cap, dan fee reserve; tidak membuat order/transaksi.
- Tes: `uv run python -m unittest tests.test_risk tests.test_no_execution` — 3/3 lulus.

Berikutnya: M5.2 reservation simulator.
