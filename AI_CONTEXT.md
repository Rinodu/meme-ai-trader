# Context aktif

Pembaruan: 2026-09-16 setelah M4.1.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M3 selesai; M4.1 menyediakan snapshot fitur deterministik point-in-time dengan warm-up. M3 tetap fail-closed untuk `UNKNOWN`/`REJECT`.
- Bukti terbaru: 31/31 tes lulus pada Python 3.12 dan PostgreSQL lokal; data future tidak masuk fitur, baseline harga nol/history kurang tidak ready, dan data optional hilang tidak diubah menjadi nol.
- Branch kerja: `task/m4-1-features-warmup`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: polling/reconnect/backfill, signal strategi, signer, dan jalur transaksi.

Tugas berikut: M4.2 signal dan expiry. Detail bukti M4.1 ada di `docs/tasks/CURRENT.md`.
