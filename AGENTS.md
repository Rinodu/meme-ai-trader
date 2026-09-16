# Aturan kerja AI — Meme AI Trader

## Konteks minimum

Baca file ini, AI_CONTEXT.md, dan docs/tasks/CURRENT.md. Lalu baca bagian ROADMAP.md, FEATURES.md, serta kode/tes yang relevan. Baca PRD.md pada sesi awal atau saat scope produk berubah. BLUEPRINT.md dibaca penuh saat perencanaan arsitektur pertama; sesudah itu ambil bagian yang terkait. Jangan membaca seluruh repo atau riwayat chat tanpa kebutuhan.

Dokumen desain adalah target; kode dan hasil pemeriksaan menunjukkan keadaan aktual. Jika berbeda, laporkan dan perbarui status berdasarkan bukti. Instruksi terbaru pengguna tetap berlaku; catat perubahan keputusan tanpa mengubah instruksi platform atau mengakali izin.

## Pelaksanaan

- Satu subtugas per permintaan. Selesaikan implementasi, koreksi, pemeriksaan, dokumentasi, commit, dan push branch tugas jika remote tersedia; kemudian laporkan.
- Ikuti ketergantungan ROADMAP.md. Jangan lompat milestone atau menambah fitur di luar tugas.
- Periksa status Git, perubahan pengguna, branch, dan file aturan lain yang berlaku sebelum edit.
- Pertahankan fitur dan perilaku terdaftar. Jika diperlukan perubahan perilaku atau penghapusan fitur lama, jelaskan dampak dan minta keputusan pengguna SEBELUM perubahan tersebut. Refactor internal yang mempertahankan perilaku boleh dilakukan bila diperlukan tugas.
- Jangan menimpa pekerjaan pengguna, melakukan reset destruktif, force push, atau mengganti arsitektur tanpa alasan dan kewenangan yang jelas.
- Pakai pencarian terarah; baca pemanggil dan tes ketika mengubah kontrak modul.
- Jangan mengganti dependency, memformat seluruh repo, atau merapikan modul lain tanpa kebutuhan konkret.
- Target lingkungan Windows. Gunakan perintah PowerShell untuk panduan pengguna; jangan mengasumsikan WSL/Docker sudah tersedia.
- Komentar menjelaskan alasan/invarian yang tidak jelas, bukan mengulang setiap baris kode.

## Verifikasi dan perlindungan

Gunakan TESTING.md. Jangan melemahkan assertion, menghapus tes, atau menyamarkan mock sebagai integrasi asli untuk membuat hasil lulus. Risk, saldo, transaksi, exit, dan migrasi memerlukan pengujian dampak yang relevan. Catat pemeriksaan yang tidak dapat dijalankan beserta penyebabnya. Jangan menandai DONE jika gate wajib belum terpenuhi.

Runtime hanya collect_only, replay, dan paper_signal. Tidak boleh ada jalur membuat, menandatangani, atau mengirim transaksi; private key/signer tidak termasuk konfigurasi proyek. Jupiter hanya boleh dipakai sebagai simulator quote/biaya. API key tidak dibaca ke chat/log atau disimpan di Git.

## Dokumentasi dan Git

Perbarui CURRENT.md dan AI_CONTEXT.md pada setiap serah terima. FEATURES.md hanya jika perilaku/status/bukti berubah; ROADMAP.md jika status berubah; CHANGELOG.md untuk perubahan selesai; ADR jika keputusan arsitektur berubah. Jangan menduplikasi uraian panjang.

Ikuti GIT_WORKFLOW.md: commit perubahan tugas yang sudah diverifikasi dan push ke branch tugas pada remote yang telah dikonfigurasi/ditentukan pengguna. Pengguna telah mengizinkan commit dan push branch tugas; tidak perlu meminta ulang untuk tiap tugas. Merge ke main menunggu instruksi eksplisit. Aktivasi trading live tidak berada dalam scope signal bot. Jika remote/autentikasi belum ada, selesaikan pekerjaan lokal yang mungkin dan laporkan hambatannya.

## Hemat token

Satu agen secara default; jangan delegasi tanpa permintaan pengguna. Gunakan konteks minimum yang memadai, output pencarian/log terbatas, dan patch terarah. Jangan cetak ulang source lengkap saat mengedit file langsung kecuali diminta. Baca TOKEN_POLICY.md hanya ketika perlu detail anggaran. Jangan mengklaim jumlah token yang tidak tersedia dari alat.

## Laporan akhir

Ringkas: perubahan; fitur terdampak; pemeriksaan/hasil; keterbatasan; commit/push; subtugas berikutnya. Jangan mengklaim push/tes/fitur selesai tanpa bukti. Setelah satu subtugas selesai, jangan otomatis mulai subtugas berikutnya.

## Checklist progres wajib

Ikuti PROGRESS.md sebagai sumber status subtugas. Baca ringkasan dan bagian milestone aktif saja. Setelah subtugas selesai/terhambat, perbarui status, checkbox, hitungan, dan satu baris riwayat bermakna. SELESAI hanya berdasarkan acceptance criteria dan bukti pemeriksaan; AI menetapkannya tanpa approval rutin. Sinkronkan ringkasan ROADMAP.md/AI_CONTEXT.md tanpa menyalin detail.

Jika fitur selesai rusak, ubah tugas menjadi DIBUKA_KEMBALI dan buka status fitur/gate terdampak. Prioritaskan perbaikan sebelum fitur baru. Pertahankan bukti lama; arsipkan CURRENT.md sebagai docs/tasks/Mx.y.md ketika berganti tugas.

Laporan akhir menyertakan checklist singkat: ID/status tugas, tes, commit/push, progres selesai/total/persen, hambatan, dan satu langkah berikutnya. Hindari mencetak seluruh checklist. Push yang gagal tetap dilaporkan; jangan memalsukan status atau membuat loop commit untuk mencatat SHA sendiri.

## Scope signal-only

Baca SIGNAL_BOT_SCOPE.md bila mengubah strategy, Telegram, simulator, atau credential. Pilih nol/satu kandidat terbaik per siklus sesuai aturan yang dapat diuji; jangan memaksa sinyal. Score tidak boleh dinamai probabilitas kecuali model memiliki kalibrasi dan bukti evaluasi. Setiap sinyal harus memiliki alasan exit dan maksimal hold; tidak ada executor/signer/submission.
