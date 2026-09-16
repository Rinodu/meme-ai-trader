# Changelog

## M10.2 — 2026-09-16
- Menambahkan validasi payload lokal terhadap quote, signer, dan destination.
- 52/52 tes lulus pada PostgreSQL lokal; tanpa RPC atau signing.

## M10.1 — 2026-09-16
- Menambahkan kontrak quote lokal dengan validasi route dan usia.
- 51/51 tes lulus pada PostgreSQL lokal; tanpa provider atau transaksi.

## M9.3 — 2026-09-16
- Menambahkan forward paper sebagai record tervalidasi tanpa transport atau submit.
- 50/50 tes lulus pada PostgreSQL lokal.

## M9.2 — 2026-09-16
- Menambahkan approval one-time dengan binding intent/token/side/nominal dan TTL.
- 49/49 tes lulus pada PostgreSQL lokal; tanpa transport Telegram atau signing.

## M9.1 — 2026-09-16
- Menambahkan allowlist eksplisit sender dan command tanpa koneksi bot.
- 48/48 tes lulus pada PostgreSQL lokal; tanpa approval atau eksekusi.

## M8.3 — 2026-09-16
- Menambahkan metrik expectancy, profit factor, dan drawdown berstatus `INCONCLUSIVE`.
- 47/47 tes lulus pada PostgreSQL lokal; tanpa klaim strategi layak.

## M8.2 — 2026-09-16
- Menambahkan split kronologis development, validation, dan holdout.
- 46/46 tes lulus pada PostgreSQL lokal; holdout tidak dipakai untuk tuning.

## M8.1 — 2026-09-16
- Menambahkan fingerprint stabil untuk version dan parameter eksperimen.
- 45/45 tes lulus pada PostgreSQL lokal; tanpa tuning otomatis atau akses holdout.

## M7.3 — 2026-09-16
- Menambahkan label TP/SL/time-out dan status no-route/data insufficient yang eksplisit.
- 44/44 tes lulus pada PostgreSQL lokal; tanpa fill atau transaksi.

## M7.2 — 2026-09-16
- Menambahkan cost model basis point untuk fee, slippage, dan impact tanpa parameter default.
- 43/43 tes lulus pada PostgreSQL lokal; tanpa fill atau transaksi.

## M7.1 — 2026-09-16
- Memverifikasi replay time-ordered untuk input out-of-order berdasarkan `received_at`.
- 42/42 tes lulus pada PostgreSQL lokal; tanpa cost, fill, atau transaksi.

## M6.3 — 2026-09-16
- Menambahkan daftar intent/attempt pending untuk restart dan menahan replacement attempt sampai reconciliation.
- 41/41 tes lulus pada PostgreSQL lokal; tidak ada RPC, signing, atau submit.

## M6.2 — 2026-09-16
- Menambahkan lifecycle tervalidasi untuk intent/attempt dan penolakan transisi terminal.
- 40/40 tes lulus pada PostgreSQL lokal; tidak ada signing atau submit.

## M6.1 — 2026-09-16
- Menambahkan ledger PostgreSQL intent dan attempt dengan ID serta status awal terpisah.
- 39/39 tes lulus pada PostgreSQL lokal; tidak ada signing atau submit.

## M5 — 2026-09-16
- Menambahkan sizing/exposure, reservation atomik, dan mode exit/kill switch.
- 38/38 tes lulus pada PostgreSQL lokal; tidak ada signing atau transaksi.

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
