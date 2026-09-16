# M2.3 — Adapter Birdeye read-only

Status: SELESAI pada 2026-09-16.

- Adapter meminta Token Overview melalui HTTP GET, menormalisasi snapshot menjadi raw event, dan tidak mengarang identity atau waktu event.
- Respons provider invalid aman dan API key tidak muncul dalam error.
- Tes: `uv run python -m unittest tests.test_birdeye tests.test_raw_events_integration` — 15/15 lulus pada PostgreSQL lokal.

Berikutnya: M2.4 quality dan reconciliation feed.
