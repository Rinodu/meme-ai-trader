# Context aktif

Pembaruan: 2026-09-16 setelah M8.2.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M7 selesai; M8.1–M8.2 membekukan eksperimen dan memisahkan development/validation/holdout secara kronologis.
- Bukti terbaru: 46/46 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m8-2-walk-forward-holdout`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: backtest, signer, dan jalur transaksi.

Tugas berikut: M8.3 stress/report. Detail bukti M8.2 ada di `docs/tasks/CURRENT.md`.
