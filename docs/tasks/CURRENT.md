# Dokumentasi workflow dan setup provider

Status: SELESAI pada 2026-09-21.

- Diagram workflow target dan alur keputusan fail-closed tersedia di
  `docs/WORKFLOW_SETUP.md`.
- Setup Windows menggunakan environment proses; `.env` tidak diklaim dimuat
  otomatis.
- Pemakaian provider dan Telegram TEST dipisahkan dan dibatasi satu provider per
  proses sampai smoke runner mendukung pemilihan provider secara eksplisit.
- Dokumen tidak mengubah status milestone `40/40` dan tidak menyatakan provider
  atau bot siap produksi.
- Temuan sweep tetap terbuka sampai source, test, dan smoke nyata membuktikan
  perbaikannya.

Berikutnya: perbaiki blocker hasil sweep lalu jalankan checklist verifikasi di
`docs/WORKFLOW_SETUP.md`.
