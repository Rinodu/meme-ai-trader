# M6.3 — Restart/reconciliation simulator

Status: SELESAI pada 2026-09-16.

- Restart memuat intent/attempt pending; replacement attempt ditolak hingga attempt lama direkonsiliasi.
- Tes: `uv run python -m unittest tests.test_raw_events_integration tests.test_no_execution` — 14/14 lulus pada PostgreSQL lokal.

Berikutnya: M7.1 time replay.
