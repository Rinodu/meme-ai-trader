# M1.2 — Kerangka/config Signal Bot

Status: SELESAI pada 2026-09-16.

## Lingkup dan bukti

- Runtime menerima hanya `collect_only`, `replay`, dan `paper_signal`; mode live ditolak.
- Startup `python -m meme_ai_trader` berhasil untuk ketiga mode tanpa credential trading.
- `.env.example` mendokumentasikan mode aman dan hanya key data Birdeye opsional.
- Tes: `uv run python -m unittest tests.test_config` — 5/5 lulus.

Berikutnya M1.3 menutup gate konfigurasi Signal Bot dan regresi no-execution.
