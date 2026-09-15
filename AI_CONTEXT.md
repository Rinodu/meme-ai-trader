# Kondisi aktual

Pembaruan 15 September 2026 setelah M2.1.

- Target tetap full automation Solana secara bertahap, Telegram dahulu, dengan default awal `collect_only` dan tanpa aktivasi live otomatis.
- M1 selesai dan M2 berjalan: M2.1 selesai. Progres resmi 4/40 subtugas (10,0%); 1/13 milestone selesai.
- Konfigurasi tetap default `collect_only`. PostgreSQL raw-event schema dan repository append-only tersedia; belum ada deduplikasi, collector, strategi, signer, atau jalur transaksi.
- Git identity dan remote `origin` tersedia. M1.1 `84c944b`; M1.2 `2b34cd2`; M1.3 `ce9c273`. M2.1 dikerjakan pada branch `task/m2-1-raw-repository`.
- Project dipin ke Python 3.12 melalui `uv`; Psycopg 3.3.5 dikunci di `uv.lock`.
- PostgreSQL 18.6 lokal aktif sebagai service `postgresql-x64-18` pada `localhost:5432`. Password tetap lokal dan tidak disimpan di repository/chat.
- Enam tes lulus pada runtime project dengan PostgreSQL nyata: lima regresi config M1 dan satu migration/round-trip M2.1. Serena mengenali simbol; Pyright Serena belum mengikuti `.venv` untuk resolusi import Psycopg. RTK 0.48.0 tersedia dan integrasi Codex lokal berada di `RTK.md`.
- API key/private key tidak diminta atau dibaca. Anggaran subscription baru tetap Rp0; modal serta parameter live belum ditetapkan.
- Serena aktif dan onboarding tersimpan di `.serena/`; cache serta konfigurasi mesin lokal diabaikan Git.
- Tugas berikutnya: M2.2, deduplikasi dan semantics timestamp/event terlambat.

Detail tugas lama di arsip `docs/tasks/`; bukti M2.1 di `docs/tasks/CURRENT.md`.
