# Context aktif

Pembaruan: 2026-09-16 setelah M3.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M3 selesai. M3 menambahkan universe filter deterministik, security evidence fail-closed, dan audit entry yang hanya mengizinkan universe eligible + security `PASS`.
- Bukti terbaru: 27/27 tes lulus pada Python 3.12 dan PostgreSQL lokal; nol tetap valid, feed stale/partial/tidak ada tidak ready, dan `UNKNOWN`/`REJECT` memblokir entry.
- Branch kerja: `task/m3-3-entry-gate-audit`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: polling/reconnect/backfill, fitur/sinyal strategi, signer, dan jalur transaksi.

Tugas berikut: M4.1 fitur deterministik dan warm-up point-in-time. Detail bukti M3 ada di `docs/tasks/`.
