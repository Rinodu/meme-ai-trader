# M11.2 — Deviasi paper

Status: SELESAI pada 2026-09-21.

- Kontrak `compare` membandingkan outcome sinyal dan paper tanpa eksekusi atau probabilitas.
- Status output dibatasi ke `MATCH`, `DEVIATION`, dan `INSUFFICIENT_DATA`.
- Signal window inklusif dimulai dari `signal_timestamp` dan default 3600 detik.
- Tes penuh: `uv run python -m unittest discover -s tests -v` — 60/60 lulus.
- Detail kontrak: `docs/tasks/M11.2.md`.

Berikutnya: M11.3 laporan kualitas.
