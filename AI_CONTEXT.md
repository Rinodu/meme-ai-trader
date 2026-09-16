# Context aktif

Pembaruan: 2026-09-16 setelah M6.1.

- Mode tetap `collect_only`; belum ada collector aktif, signer, atau transaksi.
- M1–M5 selesai; M6.1 menambah ledger PostgreSQL dengan `execution_intents` dan `execution_attempts` ber-ID terpisah.
- Bukti terbaru: 39/39 tes lulus pada Python 3.12 dan PostgreSQL lokal.
- Branch kerja: `task/m6-1-intent-attempt`; remote `origin` tersedia.
- PostgreSQL lokal tersedia; password tetap lokal dan tidak masuk source/Git/log.
- Batas yang belum diimplementasikan: state machine execution, restart/reconciliation, signer, dan jalur transaksi.

Tugas berikut: M6.2 state machine. Detail bukti M6.1 ada di `docs/tasks/CURRENT.md`.
