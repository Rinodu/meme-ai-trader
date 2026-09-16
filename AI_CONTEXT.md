# Context aktif

Pembaruan: 2026-09-16 setelah M4.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M4 selesai; M4 memiliki fitur point-in-time, signal expiry, dan replay deterministik.
- Bukti terbaru: 35/35 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m4-3-deterministic-replay`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: polling/reconnect/backfill, risk, signer, dan jalur transaksi.

Tugas berikut: M5.1 sizing/exposure. Detail bukti M4.3 ada di `docs/tasks/CURRENT.md`.
