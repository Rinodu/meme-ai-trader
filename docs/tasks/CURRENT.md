# M2.1 — Schema dan raw-event repository

Status: SELESAI pada 2026-09-15. Prasyarat: M1 selesai pada commit `ce9c273`.

## Tujuan dan lingkup

Tambahkan schema PostgreSQL pertama dan repository append-only minimum untuk menyimpan raw market event. Lingkup tidak mencakup deduplikasi/event ordering (M2.2), adapter Birdeye (M2.3), atau rekonsiliasi feed (M2.4).

## Acceptance criteria

- PostgreSQL lokal terverifikasi aktif; dependency Psycopg dikunci dan project memakai Python 3.12 lokal.
- Migration idempotent membuat tabel `raw_events` dengan tipe PostgreSQL yang tepat: UTC-aware timestamps, `numeric`, `jsonb`, array missing fields, dan constraint dasar nonnegatif.
- Schema memuat field inti blueprint tanpa menyamakan data hilang dengan nol.
- Repository hanya menyediakan insert raw event dan mengembalikan ID database; transaksi tetap dikendalikan caller.
- Integration test PostgreSQL membuktikan migration dapat dijalankan ulang dan round-trip mempertahankan nilai inti, raw JSON, `NULL`, serta nol.
- Tes konfigurasi M1 tetap lulus; tidak ada koneksi provider atau transaksi blockchain.
- Dokumentasi/checklist diperbarui; commit/push branch tugas dilakukan.

## Pemeriksaan

Jalankan seluruh unit test, integration test pada PostgreSQL lokal dengan credential yang dimasukkan pengguna di terminal aman, diagnostics Serena, diff check, dan status Git.

## Bukti

- PostgreSQL 18.6 terpasang; service `postgresql-x64-18` aktif dan `localhost:5432` menerima koneksi.
- Psycopg 3.3.5 dikunci oleh `uv`; `.python-version` dan virtualenv lokal memakai Python 3.12.10.
- Migration `001_raw_events.sql` berhasil dijalankan dua kali pada schema tes PostgreSQL tanpa konflik.
- Integration test membuktikan insert/ID database serta round-trip `timestamptz`, `numeric(0)`, `NULL`, `text[]`, dan `jsonb`.
- `uv run python -m unittest discover -s tests -v`: 6 tes lulus pada PostgreSQL lokal, tanpa skip; 5 tes konfigurasi M1 tetap lulus.
- Repository tidak melakukan commit internal; caller mengendalikan transaksi. Tidak ada provider atau blockchain yang dipanggil.
- Serena mengenali simbol baru; Pyright Serena melaporkan import Psycopg tidak resolved karena interpreter server tidak mengikuti `.venv`, tetapi import dan integration test melalui runtime project lulus.
- `git diff --check`, status/staged diff, commit, dan push diverifikasi pada penutupan tugas.

## Serah terima

Schema dan repository raw append-only tersedia. M2.2 berikutnya tetap bertanggung jawab pada deduplikasi dan perilaku timestamp/event terlambat.
