# M9.1 — Telegram allowlist/commands

Status: SELESAI pada 2026-09-16.

- Sender dan command harus melalui allowlist eksplisit.
- Capability approval buy/sell legacy dihapus; guard no-execution menolak kemunculannya kembali.
- Tes: `uv run python -m unittest tests.test_telegram tests.test_no_execution` — 3/3 lulus.

Berikutnya: M9.2 signal dan exit update Telegram.
