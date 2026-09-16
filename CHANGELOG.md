# Changelog

## M4.3 — 2026-09-16
- Menambahkan replay deterministik dari event point-in-time dan signal policy yang sama.
- 35/35 tes lulus pada PostgreSQL lokal; tanpa fill atau transaksi.

## M4.2 — 2026-09-16
- Menambahkan baseline signal dari fitur ready dengan threshold dan expiry policy eksplisit.
- 34/34 tes lulus pada PostgreSQL lokal; tidak ada risk atau transaksi.

## M4.1 — 2026-09-16
- Menambahkan snapshot return harga, perubahan likuiditas, dan akselerasi volume dengan batas `as_of` dan warm-up eksplisit.
- 31/31 tes lulus pada PostgreSQL lokal; tidak ada signal atau transaksi.

## M3 — 2026-09-16
- Menambahkan filter universe point-in-time, security evidence fail-closed, dan audit keputusan entry.
- 27/27 tes lulus pada PostgreSQL lokal; tidak ada quote, signer, atau transaksi.

## M2.4 — 2026-09-15
- Menambahkan assessment freshness/field wajib dan rekonsiliasi raw event terbaru sesuai `as_of`.
- 17 tes lulus pada PostgreSQL lokal; scheduler, retry loop, WebSocket, dan transaksi tidak ditambahkan.

## M2.3 — 2026-09-15
- Adapter Birdeye Token Overview GET read-only dan normalisasi snapshot raw event.
- 13 tes lulus pada PostgreSQL lokal; tidak ada transaksi atau secret tersimpan.

## M2.2 — 2026-09-15
- Dedup identitas event, UTC timestamp, dan query point-in-time.

## M2.1 — 2026-09-15
- Schema PostgreSQL dan repository raw event append-only.

## M1 — 2026-09-15
- Konfigurasi Python `collect_only` dan gate validasi.
