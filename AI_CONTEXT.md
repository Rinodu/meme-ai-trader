# Context aktif

Pembaruan: 2026-09-16 setelah M4.2.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M3 selesai; M4.1 menyediakan fitur point-in-time/warm-up dan M4.2 signal threshold dengan expiry deterministik. M3 tetap fail-closed untuk `UNKNOWN`/`REJECT`.
- Bukti terbaru: 34/34 tes lulus pada Python 3.12 dan PostgreSQL lokal; signal tidak aktif pada batas expiry dan tidak terbit dari fitur tidak ready.
- Branch kerja: `task/m4-2-signal-expiry`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: polling/reconnect/backfill, replay strategi, signer, dan jalur transaksi.

Tugas berikut: M4.3 replay deterministik. Detail bukti M4.2 ada di `docs/tasks/CURRENT.md`.
