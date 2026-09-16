# Context aktif

Pembaruan: 2026-09-16 setelah M10.1.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M9 selesai; M10.1 menyediakan kontrak quote lokal dengan validasi route dan usia.
- Bukti terbaru: 51/51 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m10-1-quote-route`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: backtest, signer, dan jalur transaksi.

Tugas berikut: M10.2 decode/simulation. Detail bukti M10.1 ada di `docs/tasks/CURRENT.md`.
