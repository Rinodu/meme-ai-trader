# Kondisi aktual

Pembaruan 15 September 2026 setelah M2.3.

- Target tetap full automation Solana secara bertahap, Telegram dahulu, dengan default awal `collect_only` dan tanpa aktivasi live otomatis.
- M1 selesai dan M2 berjalan: M2.1/M2.2/M2.3 selesai. Progres resmi 6/40 subtugas (15,0%); 1/13 milestone selesai.
- Konfigurasi tetap default `collect_only`. PostgreSQL raw-event schema/repository memiliki dedup identitas dan pembacaan point-in-time; belum ada collector, strategi, signer, atau jalur transaksi.
- Git identity dan remote `origin` tersedia. M1.1 `84c944b`; M1.2 `2b34cd2`; M1.3 `ce9c273`; M2.1 `c27ec8e`. M2.2 pada branch `task/m2-2-dedup-timestamps` dari basis M2.1 terbaru.
- Project dipin ke Python 3.12 melalui `uv`; Psycopg 3.3.5 dikunci di `uv.lock`.
- PostgreSQL 18.6 lokal aktif sebagai service `postgresql-x64-18` pada `localhost:5432`. Password tetap lokal dan tidak disimpan di repository/chat.
- Sembilan tes lulus pada runtime project dengan PostgreSQL nyata: lima regresi config M1 dan empat integration test M2. Serena mengenali simbol; Pyright Serena belum mengikuti `.venv` untuk resolusi import Psycopg. RTK 0.48.0 tersedia dan integrasi Codex lokal berada di `RTK.md`.
- API key/private key tidak diminta atau dibaca. Anggaran subscription baru tetap Rp0; modal serta parameter live belum ditetapkan.
- Serena aktif dan onboarding tersimpan di `.serena/`; cache serta konfigurasi mesin lokal diabaikan Git.
- M2.3 pada `task/m2-3-birdeye-adapter` menambahkan adapter Birdeye GET read-only dan normalisasi snapshot tanpa mengarang event identity/time; 13 tes lulus pada PostgreSQL lokal. M2.4 berikutnya: quality dan rekonsiliasi feed.

Detail tugas lama di arsip `docs/tasks/`; bukti M2.2 di `docs/tasks/CURRENT.md`.
