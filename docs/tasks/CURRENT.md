# M4.1 — Fitur deterministik dan warm-up

Status: SELESAI pada 2026-09-16. Basis: M3 terverifikasi.

## Lingkup

Bangun snapshot fitur point-in-time dari raw event yang tersedia. Tugas ini menetapkan warm-up serta perilaku data hilang; tidak membuat signal, entry, risk, quote, signer, atau transaksi.

## Acceptance criteria

- Hanya event dengan `received_at <= as_of` yang digunakan.
- Snapshot membutuhkan jumlah sampel harga valid sesuai warm-up; data kurang atau harga baseline nol menghasilkan status tidak ready yang eksplisit.
- Return harga, perubahan likuiditas, dan akselerasi volume dihitung deterministik; input data hilang menghasilkan `None`, bukan nol buatan.
- Tes mencakup batas point-in-time, warm-up, nol/missing, dan pembacaan repository PostgreSQL nyata.

## Bukti

- `uv run python -m unittest tests.test_quant`: 3 tes lulus.
- `uv run python -m unittest tests.test_raw_events_integration`: 8 tes PostgreSQL lulus.
- Suite penuh: 31/31 tes lulus pada PostgreSQL lokal, tanpa skip.
- Snapshot memakai hanya event `received_at <= as_of`; baseline harga nol dan history kurang tidak ready, sedangkan data optional hilang tetap `None`.

## Serah terima

M4.2 berikutnya: signal dan expiry. Tidak ada signal, risk, quote, signer, atau transaksi dalam M4.1.
