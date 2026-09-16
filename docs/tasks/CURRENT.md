# M4.2 — Signal dan expiry

Status: SELESAI pada 2026-09-16. Basis: M4.1 terverifikasi.

## Lingkup

Tambahkan baseline signal deterministik dari snapshot fitur siap pakai, beserta expiry eksplisit. Tidak ada sizing, risk, quote, intent, signer, atau transaksi.

## Acceptance criteria

- Signal hanya eligible dari fitur ready dan return yang mencapai threshold policy.
- Signal memiliki `expires_at` UTC yang deterministik; signal kadaluarsa tidak eligible.
- Fitur tidak ready, return hilang, dan return di bawah threshold menghasilkan alasan eksplisit.
- Tes mencakup PASS, reject, dan expiry.

## Bukti

- `uv run python -m unittest tests.test_strategy`: 3 tes lulus.
- Suite penuh: 34/34 tes lulus pada PostgreSQL lokal, tanpa skip.
- Signal hanya aktif sampai `expires_at`; expiry tepat pada batas tidak aktif.

## Serah terima

M4.3 berikutnya: replay deterministik. Risk, quote, signer, dan transaksi tetap belum tersedia.
