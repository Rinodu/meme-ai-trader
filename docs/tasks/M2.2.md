# M2.2 — Deduplikasi dan timestamp raw event

Status: SELESAI pada 2026-09-15. Basis: M2.1 `c27ec8e` beserta perbaikan/tooling berikutnya pada branch `task/m2-1-raw-repository`.

## Lingkup

Tegakkan identitas event pada PostgreSQL dan repository tanpa menimpa raw event. Pertahankan `event_time` sebagai waktu kejadian dan `received_at` sebagai waktu tersedia; event terlambat harus tetap tersimpan dan dapat dibaca dalam urutan kejadian tanpa kebocoran point-in-time. Birdeye/reconnect/quality reconciliation tetap M2.3/M2.4.

## Acceptance criteria

- Retry dengan `event_id` sama atau pasangan `(source, source_event_id)` sama tidak menambah baris; insert mengembalikan ID baris yang sudah ada.
- Migrasi dapat dijalankan ulang di schema M2.1. Jika data lama sudah melanggar identitas unik, migrasi gagal jelas tanpa menghapus raw data.
- `event_time` nullable, kedua timestamp yang tersedia harus timezone-aware dan dinormalisasi UTC; `NULL` tetap bukan nol.
- Pembacaan `received_at <= as_of` diurutkan menurut `event_time`, lalu tie-breaker stabil; event terlambat tidak muncul sebelum diterima.
- Tes PostgreSQL nyata mencakup retry, konflik identitas, timestamp naive/offset, event terlambat/out-of-order, dan regresi M1/M2.1.
- Checklist/bukti sinkron; commit dan push hanya branch tugas.

## Bukti

- Branch `task/m2-2-dedup-timestamps` dibuat dari M2.1 yang sudah dipush; perubahan lain tidak ada saat mulai.
- Migration `002_event_identity.sql`, dedup insert, validasi UTC, dan pembacaan point-in-time sudah diimplementasikan lokal.
- `rtk uv run python -m compileall -q meme_ai_trader tests` berhasil.
- Prompt pertama tidak mendapat input; proses dihentikan. Pada prompt kedua, seluruh 9 tes lulus pada PostgreSQL 18.6 nyata (`exit 0`), tanpa skip; password hanya berada di environment proses tes dan skrip sementara dihapus.
- Tes membuktikan retry kedua identitas tidak menambah baris, dua identitas yang menunjuk baris berbeda ditolak, dan migrasi menolak data duplikat lama tanpa menghapusnya.
- Tes membuktikan offset waktu dinormalisasi UTC, timestamp naive ditolak, `event_time = NULL` tetap ada, dan event terlambat baru muncul setelah `received_at` namun terurut menurut `event_time`.
- Serena hanya melaporkan import Psycopg tidak resolved oleh language server, seperti M2.1; runtime Python project dan tes PostgreSQL lulus.
- `rtk git diff --check` bersih; staged diff, commit, dan push diverifikasi saat penutupan tugas.

## Serah terima

M2.3 berikutnya menghubungkan adapter provider; tidak ada credential atau transaksi live dalam M2.2.
