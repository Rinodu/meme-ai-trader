# M10.2 — Decode/simulation

Status: SELESAI pada 2026-09-21.

- Payload diverifikasi lokal terhadap quote, authority, dan destination; simulasi tidak memanggil signer atau submit.
- Tes: `uv run python -m unittest tests.test_simulation tests.test_quotes tests.test_no_execution` — 4/4 lulus.

Berikutnya: M10.3 signer boundary/status.
