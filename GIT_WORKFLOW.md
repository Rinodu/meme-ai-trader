# Git dan pemulihan

## Siklus tugas

1. Periksa status working tree, branch, remote, dan perubahan pengguna. Jangan otomatis stash/reset perubahan orang lain.
2. Bila belum ada repo, inisialisasi lokal setelah memeriksa folder. Identitas commit menggunakan konfigurasi pengguna; jangan mengarang email.
3. Branch tugas: `task/m1-1-project-config` atau pola sejenis. Mulai dari basis yang memuat prasyarat selesai.
4. Kerjakan hanya file tugas. Jalankan tes relevan dan periksa diff untuk penghapusan fitur/rahasia.
5. Perbarui dokumen terkait lalu commit, misalnya `feat(config): add collect-only configuration`.
6. Push ke branch tugas pada remote yang telah dipilih/dikonfigurasi. Jangan push ke main atau force push. Remote hilang/login gagal: catat status LOCAL_ONLY, jangan mengklaim backup remote berhasil.
7. Laporkan commit dan push. Merge ke main menunggu instruksi pengguna. Jika tugas lanjutan diizinkan sebelum merge, dokumentasikan branch basis dan ketergantungannya.

## Pemulihan

Gunakan revert untuk membatalkan commit yang sudah dibagikan; jangan menulis ulang riwayat remote sembarangan. Tag milestone setelah gate lulus dan versi stabil benar-benar tersedia. Git hanya memulihkan kode; migrasi database memerlukan backup/forward fix, transaksi blockchain tidak dapat dibatalkan oleh Git.

## Pemeriksaan sebelum push

Jangan stage seluruh folder tanpa melihat isinya. Hindari `.env`, `.env.example` (sesuai pilihan pengguna: tetap lokal), keypair, dump database, raw dataset besar, log, cache, dan virtual environment. Commit lockfile dependency yang dipilih. Jika kebocoran ditemukan, hentikan penyebaran, laporkan, dan lakukan rotasi melalui pemilik kredensial; menghapus file saja tidak menghapus rahasia dari riwayat.
