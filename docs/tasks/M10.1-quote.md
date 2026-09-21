# M10.1 — Quote/route simulator

Status: SELESAI pada 2026-09-21.

- Kontrak quote hanya memvalidasi route, nominal/min-output, waktu quote, dan usia quote untuk simulasi kelayakan.
- Tidak ada RPC submit, signer, atau transaksi.
- Tes: `uv run python -m unittest tests.test_quotes tests.test_no_execution` — 3/3 lulus.

Berikutnya: M10.2 decode/simulation.
