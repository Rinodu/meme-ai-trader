# Context aktif

Pembaruan: 2026-09-16 setelah M7.2.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M6 selesai; M7.1–M7.2 menyediakan replay time-ordered dan estimasi biaya eksplisit fee/slippage/impact.
- Bukti terbaru: 43/43 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m7-2-cost-model`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: backtest, signer, dan jalur transaksi.

Tugas berikut: M7.3 label TP/SL/no-route. Detail bukti M7.2 ada di `docs/tasks/CURRENT.md`.
