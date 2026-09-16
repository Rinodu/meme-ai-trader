# M1.1 — Pemeriksaan awal dan kontrak lingkungan

Status: SELESAI pada 2026-09-16.

## Tujuan

Memastikan kondisi repository dan Windows diketahui sebelum membuat kerangka aplikasi, lalu menetapkan rencana implementasi M1.2 yang dapat dijalankan.

## Lingkup

Periksa folder kerja, aturan yang berlaku, source yang mungkin sudah ada, Git/status/remote, serta ketersediaan Python. Catat kebutuhan PostgreSQL untuk M2 dan Docker/WSL hanya jika relevan. Jika Codex bekerja pada host selain PC pengguna, bedakan temuan host tersebut dari kondisi Windows pengguna.

## Acceptance criteria

- Kondisi source, Git, Python, dan akses lingkungan dicatat dengan bukti atau UNKNOWN; tidak mengarang versi/instalasi.
- Tidak ada pekerjaan pengguna yang ditimpa.
- Jika repo belum ada, Git lokal boleh diinisialisasi; identity menggunakan konfigurasi pengguna.
- Branch tugas dibuat bila Git tersedia; commit/push dokumen sesuai aturan jika identity/remote memungkinkan.
- Runtime Python yang kompatibel direncanakan berdasarkan ketersediaan/dependency, tanpa upgrade global sembarangan.
- M1.2 terdefinisi: kerangka/config collect_only dan tes konfigurasi; belum implementasi trading.
- AI_CONTEXT.md dan ROADMAP.md diperbarui dengan status aktual.

## Pemeriksaan

Status working tree/remote dan deteksi versi executable yang relevan. Tidak perlu tes aplikasi karena belum ada perubahan aplikasi pada subtugas ini.

## Bukti, hasil, dan hambatan

- Source: 28 modul Python dan 23 file tes tersedia pada checkout Signal Bot.
- Lingkungan: Python 3.12.10 dan Git 2.55.0 tersedia di Windows; remote `origin` terkonfigurasi.
- Runtime scope: `collect_only`, `replay`, dan `paper_signal`; mode live ditolak.
- Tes config: `uv run python -m unittest tests.test_config` — 5/5 lulus.
- Guard scope: suite penuh 55/55 lulus pada PostgreSQL lokal; `51113e9` membuktikan runtime tanpa wallet/signing/submit.
- Hambatan: tidak ada untuk M1.1. `integration-test.log` tidak dilacak dan dipertahankan sebagai file pengguna.

## Checklist dan bukti

Status resmi: PROGRESS.md M1.1 = SELESAI. Commit/push task: pembaruan dokumentasi M1.1 dibuat pada branch ini. M1.2 berikutnya memetakan config aman ke runtime Signal Bot tanpa menambah executor.
