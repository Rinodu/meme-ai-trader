# M2.4 — Quality dan rekonsiliasi feed

Status: SELESAI pada 2026-09-16.

- Feed hanya siap jika snapshot tersedia, fresh, dan `price` serta `liquidity` tersedia; nilai nol tetap sah.
- Rekonsiliasi membaca raw event terbaru yang tersedia pada `as_of`, sehingga data masa depan tidak bocor.
- Tes: `uv run python -m unittest tests.test_feed tests.test_birdeye tests.test_raw_events_integration` — 17/17 lulus pada PostgreSQL lokal.

Berikutnya: M3.1 universe/filter.
