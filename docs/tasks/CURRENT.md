# M1.1 — Pemeriksaan awal dan kontrak lingkungan

Status: READY; belum dikerjakan. Prasyarat: paket dokumen tersedia.

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

Belum ada. Tulis ringkas setelah eksekusi. Jika alat/akses wajib tidak tersedia, status BLOCKED/PARTIAL; jangan menandai seluruh M1 selesai.

## Checklist dan bukti

Status resmi: PROGRESS.md M1.1 = BELUM_MULAI; READY di atas berarti siap dikerjakan. Setelah selesai/terhambat, isi bukti tes/commit/push, perbarui checklist dan ringkasan chat. Untuk tugas inspeksi ini, tes aplikasi boleh N/A dengan alasan; bukti inspeksi tetap wajib.
