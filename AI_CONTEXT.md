# Context aktif

Pembaruan: 2026-09-16 setelah M7.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M7 selesai; backtest memiliki replay time-ordered, cost model eksplisit, dan label exit diskret.
- Bukti terbaru: 44/44 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m7-3-outcome-labels`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: backtest, signer, dan jalur transaksi.

Tugas berikut: M8.1 freeze experiment. Detail bukti M7.3 ada di `docs/tasks/CURRENT.md`.
