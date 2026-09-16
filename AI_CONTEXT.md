# Context aktif

Pembaruan: 2026-09-16 setelah M9.1.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M8 selesai; M9.1 memvalidasi sender dan command melalui allowlist eksplisit.
- Bukti terbaru: 48/48 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m9-1-allowlist-commands`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: backtest, signer, dan jalur transaksi.

Tugas berikut: M9.2 approval TTL. Detail bukti M9.1 ada di `docs/tasks/CURRENT.md`.
