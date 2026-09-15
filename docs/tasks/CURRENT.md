# M2.3 — Adapter Birdeye

Status: TERHAMBAT pada 2026-09-15. Basis: `main` pada `c8c8c31`.

## Lingkup

Tambahkan adapter Birdeye read-only untuk snapshot token Solana dan normalisasi ke kontrak `raw_events`. Tidak ada polling collector, reconnect, backfill, transaksi, atau pembacaan credential di luar konfigurasi yang sudah ada; itu tetap M2.4 atau milestone berikutnya.

## Acceptance criteria

- Klien memanggil endpoint Birdeye Token Overview dengan `X-API-KEY` dan `x-chain: solana`, serta hanya melakukan HTTP GET.
- Respons HTTP, JSON, dan payload provider yang tidak valid menghasilkan error terarah tanpa menampilkan API key.
- Snapshot valid dapat dinormalisasi menjadi raw event dengan payload asli, `received_at` UTC, dan nilai nol tidak dianggap hilang.
- Field provider yang tidak tersedia dicatat pada `missing_fields`; adapter tidak mengarang nilai pasar atau waktu kejadian.
- Tes fixture mencakup request, error provider, pemetaan nol/null, dan kompatibilitas event dengan repository M2.2.

## Bukti

- `rtk uv run python -m unittest tests.test_birdeye tests.test_config`: 8 tes lulus.
- `rtk uv run python -m unittest discover -s tests`: 13 tes selesai; 5 tes PostgreSQL terlewati karena `PGPASSWORD` tidak tersedia pada proses ini.
- `rtk uv run python -m compileall -q meme_ai_trader tests` dan `rtk git diff --check` lulus.
- Adapter memakai HTTP GET standar-library ke Token Overview Birdeye, tanpa credential di log atau source. Snapshot tidak diberi `event_time`/`source_event_id` palsu.

## Hambatan

Tes integrasi repository yang baru membutuhkan PostgreSQL lokal dengan `PGPASSWORD` tersedia bagi proses tes. Koneksi/secret tidak dibaca atau dicetak. Jalankan tes tersebut di environment PostgreSQL yang sudah dikonfigurasi sebelum M2.3 ditandai selesai.
