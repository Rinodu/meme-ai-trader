# Changelog

## Paket dokumen 1.0 — 2026-09-15

- Menambahkan aturan kerja sesuai pilihan Edhu, roadmap M1–M13, kontrak fitur, protokol tes/Git, kebijakan token, prompt, dan task awal.
- Menyertakan BLUEPRINT.md v2 sebagai rancangan teknis.
- Semua fitur aplikasi berstatus PLANNED. Belum mengklaim implementasi, backtest, koneksi provider, atau trading berjalan.

Tambahkan entri untuk perubahan selesai: task ID, perilaku berubah, bukti pengujian, serta keterbatasan relevan. Riwayat percobaan gagal tetap berada di catatan task/insiden, tidak disamarkan sebagai rilis selesai.

## Paket dokumen 1.1 — 2026-09-15

- Menambahkan PROGRESS.md dan template form tugas, sesuai delapan pilihan checklist pengguna.
- Menyelaraskan aturan agen, roadmap, fitur, testing, PRD, prompt, dan konteks sesi.
- Persentase awal 0%; semua pekerjaan implementasi tetap belum selesai.
- Struktur, referensi lokal, kesesuaian jumlah subtugas, dan integritas ZIP diperiksa; bukan pengujian aplikasi.

## M1.1 — Pemeriksaan lingkungan/repo — 2026-09-15

- Memverifikasi project masih berupa dokumen tanpa source aplikasi atau tes runtime.
- Memverifikasi Python 3.12.10, Git 2.55.0, dan kondisi PostgreSQL/Docker/WSL pada host Windows.
- Menginisialisasi repository lokal pada branch `task/m1-1-project-config`.
- M1.1 tersimpan pada commit `84c944b` dan telah dipush ke `task/m1-1-project-config`; tidak ada perilaku aplikasi yang berubah.

## M1.2 — Kerangka/config collect-only — 2026-09-15

- Menambahkan package Python minimal tanpa dependency runtime eksternal.
- Menetapkan default `collect_only`, menolak mode tidak didukung, dan mewajibkan API key hanya saat Birdeye aktif.
- Menambahkan perlindungan rahasia, contoh environment, dan 5 tes konfigurasi yang lulus pada Python 3.11/3.12.
