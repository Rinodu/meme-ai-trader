# M1.1 — Pemeriksaan awal dan kontrak lingkungan

Status: SELESAI pada 2026-09-15. Prasyarat: paket dokumen tersedia.

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

- Source: 18 file Markdown; belum ada source aplikasi, konfigurasi runtime, atau tes aplikasi.
- Git: Git 2.55.0 tersedia; repository lokal diinisialisasi pada branch `task/m1-1-project-config`. Seluruh file masih untracked, remote belum ada, dan `user.name`/`user.email` belum dikonfigurasi, sehingga commit/push tertunda.
- Python: CPython 3.12.10 tersedia melalui `py`/`python`; CPython 3.11.16 juga tersedia melalui instalasi `uv`. Target M1.2: Python >=3.11, dikembangkan dengan 3.12.10 pada virtual environment lokal tanpa upgrade global.
- Infrastruktur: `psql` dan Docker tidak ditemukan. `wsl.exe` ada tetapi WSL belum terpasang. PostgreSQL baru dibutuhkan pada M2; metode instalasinya diputuskan sebelum M2 tanpa menjadikan Docker/WSL prasyarat M1.
- Tool efisiensi: Token Saviour, RTK, dan Serena tidak tersedia pada sesi ini; fallback yang digunakan adalah pemeriksaan PowerShell/Git dengan output terbatas.
- Pemeriksaan aplikasi: N/A karena M1.1 hanya inspeksi dan belum ada aplikasi. Tidak ada source pengguna yang ditimpa.
- Rencana M1.2: buat kerangka Python minimal, konfigurasi dengan default `collect_only`, penolakan mode tidak didukung, pemuatan credential hanya untuk fitur aktif, `.env.example` tanpa rahasia, dan satu tes konfigurasi terarah. Tidak ada jalur trading live.

## Checklist dan bukti

Status resmi: PROGRESS.md M1.1 = SELESAI. Tes aplikasi N/A dengan alasan; bukti inspeksi tersedia di atas. Commit/push berstatus tertunda sampai Git identity dan remote tersedia.
