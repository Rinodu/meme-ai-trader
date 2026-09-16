# M3.2 — Security adapter

Status: SELESAI pada 2026-09-16.

- Evidence security read-only menghasilkan `PASS`, `REJECT`, atau `UNKNOWN`; hanya `PASS` mengizinkan entry.
- Evidence hilang, stale, parsial, invalid, dari masa depan, atau provider error bersifat fail-closed (`UNKNOWN`).
- Tes: `uv run python -m unittest tests.test_security tests.test_discovery tests.test_feed` — 9/9 lulus.

Berikutnya: M3.3 gate `UNKNOWN` dan audit keputusan.
