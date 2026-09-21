# M11.3 — Laporan kualitas sinyal

Status: SELESAI pada 2026-09-21.

- M11.2 membandingkan outcome sinyal dan paper tanpa eksekusi atau probabilitas; statusnya `MATCH`, `DEVIATION`, atau `INSUFFICIENT_DATA`.
- M11.3 menghasilkan `VALID`, `INCONCLUSIVE`, atau `INSUFFICIENT_DATA` dengan sample minimum default 30.
- Rasio deviasi/coverage dibulatkan deterministik; duplicate ID dan timestamp rusak gagal validasi.
- Probabilitas hanya tersedia jika sample minimum, out-of-sample, dan kalibrasi terdokumentasi terpenuhi.
- Tes M11.3: `uv run python -m unittest tests.test_quality_report` — 10/10 lulus.
- Tes penuh: `uv run python -m unittest discover -s tests -v` — 70/70 lulus.
- Detail kontrak: `docs/tasks/M11.3.md`.

Berikutnya: M12.1 on-chain lanjutan.
