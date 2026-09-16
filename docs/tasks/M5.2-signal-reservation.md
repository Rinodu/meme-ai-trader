# M5.2 — Reservation simulator

Status: SELESAI pada 2026-09-16.

- PostgreSQL mengurangi saldo simulasi tersedia dan mencatat reservation dalam satu transaksi; release idempoten.
- Tes: `uv run python -m unittest tests.test_raw_events_integration tests.test_no_execution` — 14/14 lulus pada PostgreSQL lokal.

Berikutnya: M5.3 exit/kill switch.
