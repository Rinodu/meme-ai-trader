# Context aktif

Pembaruan: 2026-09-16 setelah M8.1.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M7 selesai; M8.1 membekukan parameter eksperimen dalam fingerprint stabil.
- Bukti terbaru: 45/45 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m8-1-freeze-experiment`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: backtest, signer, dan jalur transaksi.

Tugas berikut: M8.2 walk-forward/holdout. Detail bukti M8.1 ada di `docs/tasks/CURRENT.md`.
