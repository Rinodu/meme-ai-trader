# Context aktif

Pembaruan: 2026-09-16 setelah M6.2.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M5 selesai; M6.1–M6.2 menyediakan ledger PostgreSQL intent/attempt ber-ID terpisah dengan lifecycle tervalidasi.
- Bukti terbaru: 40/40 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m6-2-state-machine`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: restart/reconciliation execution, signer, dan jalur transaksi.

Tugas berikut: M6.3 restart/reconciliation. Detail bukti M6.2 ada di `docs/tasks/CURRENT.md`.
