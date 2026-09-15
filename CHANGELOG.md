# Changelog

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
