# M3.1 — Universe/filter

Status: SELESAI pada 2026-09-16.

- Filter kandidat memakai data point-in-time, memerlukan chain/mint/pool/token program yang diizinkan, feed siap, umur token valid, serta ambang likuiditas/volume.
- Penolakan bersifat eksplisit dan deterministik; nilai tepat pada ambang diterima.
- Tes: `uv run python -m unittest tests.test_discovery tests.test_feed` — 5/5 lulus.

Berikutnya: M3.2 security adapter.
