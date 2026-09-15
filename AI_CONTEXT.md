# Context aktif

Pembaruan: 2026-09-15 setelah M2.4.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1 dan M2 selesai. M2.3 menyediakan adapter Birdeye GET read-only; M2.4 menyediakan assessment freshness/field wajib dan rekonsiliasi event terbaru point-in-time.
- Bukti terbaru: 17 tes lulus pada Python 3.12 dan PostgreSQL lokal; nol tetap valid, feed stale/partial/tidak ada tidak ready.
- Branch kerja: `task/m2-4-feed-quality`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: polling, reconnect, backfill, kualitas feed, rekonsiliasi, strategi, signer, dan jalur transaksi.

Tugas berikut: M3.1 universe/filter. Detail bukti M2.4 ada di `docs/tasks/CURRENT.md`.
