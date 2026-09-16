# M2.1 — Schema/raw repository Signal Bot

Status: SELESAI pada 2026-09-16.

## Bukti

- PostgreSQL `raw_events` menyimpan identitas sumber, chain/mint/pool, waktu event/terima, harga, likuiditas, volume, quality dan payload mentah.
- Migration bersifat additive dan repository menormalisasi timestamp UTC.
- Tes integrasi raw repository berjalan melalui suite penuh 55/55 pada PostgreSQL lokal.

Berikutnya M2.2 menutup dedup dan timestamp sebagai kontrak Signal Bot.
