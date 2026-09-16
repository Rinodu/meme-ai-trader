# M6.1 — Intent/attempt simulator

Status: SELESAI pada 2026-09-16.

- Ledger simulator memisahkan identitas intent dan attempt di PostgreSQL; guard Signal Bot meniadakan signing/submit.
- Tes: `uv run python -m unittest tests.test_raw_events_integration tests.test_no_execution` — 14/14 lulus pada PostgreSQL lokal.

Berikutnya: M6.2 state machine simulator.
