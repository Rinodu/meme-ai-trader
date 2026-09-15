# M2.4 — Quality dan rekonsiliasi feed

Status: SELESAI pada 2026-09-15. Basis: M2.3 terverifikasi.

## Lingkup

Tambahkan satu jalur koleksi Birdeye read-only, evaluasi freshness dan field wajib, serta rekonsiliasi terhadap raw event terbaru tersimpan. Tidak ada scheduler, retry loop, WebSocket, backfill, transaksi, atau perubahan mode aplikasi.

## Acceptance criteria

- Satu snapshot Birdeye dapat dipetakan, dinilai, dan disimpan melalui repository M2.2.
- Feed hanya ready bila event tersedia, `received_at` masih dalam batas umur, serta `price` dan `liquidity` tersedia; nol tetap valid.
- Rekonsiliasi membaca raw event terbaru per token tanpa memakai event masa depan.
- Tidak ada event terbaru menghasilkan status tidak ready yang eksplisit.
- Tes mencakup feed fresh, stale, partial, nol, tidak ada event, dan repository PostgreSQL nyata.

## Bukti

- `rtk uv run python -m unittest tests.test_feed tests.test_birdeye`: 5 tes lulus.
- `rtk proxy powershell -NoProfile -Command '<PGPASSWORD lokal>; uv run python -m unittest tests.test_raw_events_integration'`: 7 tes PostgreSQL lulus.
- Suite penuh: 17 tes lulus pada PostgreSQL lokal, tanpa skip.
- `latest_for_mint` membatasi `received_at <= as_of`; assessment membedakan tidak ada feed, stale, field wajib hilang, dan nilai nol valid.

## Serah terima

M2 selesai. M3.1 berikutnya menangani universe/filter; scheduler, retry, WebSocket, dan backfill tidak ditambahkan.
