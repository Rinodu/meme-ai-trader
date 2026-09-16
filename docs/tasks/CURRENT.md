# M2.2 — Dedup/timestamps Signal Bot

Status: SELESAI pada 2026-09-16.

- Dedup memakai `event_id` maupun identitas provider; konflik tidak mengubah raw data.
- `event_time` dan `received_at` dipisahkan, timezone-aware, serta event terlambat tidak terlihat sebelum diterima.
- Tes: `uv run python -m unittest tests.test_raw_events_integration` — 12/12 lulus pada PostgreSQL lokal.

Berikutnya M2.3 adapter Birdeye read-only.
