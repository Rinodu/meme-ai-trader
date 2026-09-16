# Context aktif

Pembaruan: 2026-09-16 setelah M9.2.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M8 selesai; M9.1–M9.2 memvalidasi allowlist dan approval yang one-time serta ber-TTL.
- Bukti terbaru: 49/49 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m9-2-approval-ttl`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: backtest, signer, dan jalur transaksi.

Tugas berikut: M9.3 forward paper. Detail bukti M9.2 ada di `docs/tasks/CURRENT.md`.
