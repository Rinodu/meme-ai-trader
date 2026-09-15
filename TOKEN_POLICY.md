# Kebijakan efisiensi token

## Coding

Sasaran: biaya per tugas selesai dan tervalidasi. Tidak ada jaminan persentase penghematan; ukur dari usage yang benar-benar tersedia.

- AGENTS.md singkat dan stabil. AI_CONTEXT.md sekitar 300–500 kata. CURRENT.md hanya satu tugas aktif; detail selesai diarsipkan bila berguna.
- Baca tiga file pintu masuk lalu bagian kode/dokumen relevan; jangan mengulang seluruh blueprint setiap sesi.
- Gunakan pencarian terarah dan batasi output. Jangan dump dependency, lockfile besar, raw dataset, log panjang atau seluruh repo ke percakapan.
- Satu agen default; delegasi hanya atas permintaan pengguna dengan manfaat dan lingkup konkret.
- Patch kecil; tanpa refactor, dependency upgrade, atau formatting massal di luar tugas.
- Simpan hasil pemeriksaan dan referensikan bukti; ulang hanya bila kode/dampak berubah atau gate mewajibkan.
- Riset API saat kontrak/provider perlu diverifikasi, bukan untuk fakta proyek yang sudah diketahui. Simpan link dan tanggal verifikasi di catatan integrasi.
- Tidak perlu menampilkan source lengkap ketika file sudah diedit langsung. Bila pengguna meminta kode untuk copy-paste, berikan file lengkap yang diminta.
- Laporan akhir ditargetkan 150–250 kata; perluas hanya untuk keputusan/masalah penting.
- Jangan mengorbankan pembacaan dependency atau tes berisiko untuk memenuhi target panjang.

## LLM dalam bot

LLM disabled sampai milestone evaluasinya. Indikator, sizing, risk, dan lifecycle memakai kode deterministik.

Saat diaktifkan: filter kandidat dahulu; deduplikasi sumber; ringkas input berbasis bukti; cache berdasarkan mint + versi prompt/model + hash bukti dan TTL. Analisis ulang ketika perubahan material atau expiry. Batasi input/output dan retry melalui konfigurasi; output dipotong tidak boleh dianggap valid otomatis.

Catat input/output/cached tokens dan biaya jika provider menyediakannya. Jika tidak tersedia, beri label perkiraan, jangan mengarang usage. Jumlah panggilan serta budget harian harus mempunyai penghentian di aplikasi, tidak hanya alert provider. Kegagalan LLM tidak mematikan exit. Baseline tanpa sosial hanya boleh menjadi fallback bila telah diuji.

Anggaran berbayar awal Rp0. Akses gratis tidak menjamin seluruh fitur tersedia. Jika biaya diperlukan, dokumentasikan pilihan dan konsekuensi sebelum pembelian/aktivasi.
