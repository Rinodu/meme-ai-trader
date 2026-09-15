# Context aktif

Pembaruan: 2026-09-15 setelah M2.3.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1 dan M2.1–M2.3 selesai. M2.3 menyediakan adapter Birdeye Token Overview GET read-only serta normalisasi snapshot ke `raw_events`.
- Bukti terbaru: 13 tes lulus pada Python 3.12 dan PostgreSQL lokal; adapter menolak respons invalid tanpa membocorkan key, serta membedakan nol dari data hilang.
- Branch kerja: `task/m2-3-birdeye-adapter`, commit terbaru `2d0dd33`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: polling, reconnect, backfill, kualitas feed, rekonsiliasi, strategi, signer, dan jalur transaksi.

Tugas berikut: M2.4 quality dan rekonsiliasi feed. Detail bukti M2.3 ada di `docs/tasks/CURRENT.md`.
