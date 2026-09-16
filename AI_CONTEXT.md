# Context aktif

Pembaruan: 2026-09-16 setelah M6.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M6 selesai; ledger PostgreSQL menyediakan intent/attempt ber-ID terpisah, lifecycle tervalidasi, dan daftar kerja pending saat restart.
- Bukti terbaru: 41/41 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m6-3-reconciliation`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: backtest, signer, dan jalur transaksi.

Tugas berikut: M7.1 time replay. Detail bukti M6.3 ada di `docs/tasks/CURRENT.md`.
