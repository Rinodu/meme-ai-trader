# M4.2 — Sinyal dan expiry

Status: SELESAI pada 2026-09-16.

- Sinyal deterministik hanya eligible dari fitur siap dan return yang memenuhi ambang; expiry UTC tepat pada batas tidak lagi aktif.
- Tes: `uv run python -m unittest tests.test_strategy tests.test_quant tests.test_no_execution` — 8/8 lulus.

Berikutnya: M4.3 replay deterministik.
