# Context aktif

Pembaruan: 2026-09-16 setelah M7.1.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M6 selesai; M7.1 memverifikasi replay deterministik memakai urutan ketersediaan `received_at` untuk input out-of-order.
- Bukti terbaru: 42/42 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m7-1-time-replay`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: backtest, signer, dan jalur transaksi.

Tugas berikut: M7.2 cost model. Detail bukti M7.1 ada di `docs/tasks/CURRENT.md`.
