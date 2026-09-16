# M6.2 — State machine simulator

Status: SELESAI pada 2026-09-16.

- Lifecycle intent/attempt simulator menolak transisi invalid maupun perubahan status terminal.
- Tes: `uv run python -m unittest tests.test_raw_events_integration tests.test_no_execution` — 14/14 lulus pada PostgreSQL lokal.

Berikutnya: M6.3 restart/reconciliation simulator.
