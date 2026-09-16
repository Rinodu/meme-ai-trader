# M9.2 — Signal dan update exit Telegram

Status: SELESAI pada 2026-09-16.

- Formatter sinyal manual memuat identitas token, alasan/bukti, entry, stop, target, exit, maksimum hold, exit awal, expiry, serta score/evidence quality yang bukan probabilitas.
- Tes: `uv run python -m unittest tests.test_signal_message tests.test_telegram tests.test_no_execution` — 4/4 lulus.

Berikutnya: M9.3 forward paper signal.
