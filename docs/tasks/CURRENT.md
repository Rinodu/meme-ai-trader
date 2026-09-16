# M4.1 — Fitur/warm-up point-in-time

Status: SELESAI pada 2026-09-16.

- Snapshot fitur hanya memakai event yang tersedia pada `as_of`; warm-up kurang dan baseline nol gagal eksplisit, sementara data optional hilang tetap `None`.
- Tes: `uv run python -m unittest tests.test_quant tests.test_raw_events_integration` — 15/15 lulus pada PostgreSQL lokal.

Berikutnya: M4.2 sinyal dan expiry.
