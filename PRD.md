# Product requirements

## Target

Meme AI Trader membantu menemukan, menyaring, menguji, dan mengeksekusi peluang momentum token Solana. Target akhir full automation; kualitas setiap langkah dibuktikan sebelum melanjutkan. Keberhasilan produk mencakup ketepatan data, ketahanan eksekusi, audit, dan hasil strategi setelah biaya. Tidak ada target win rate atau profit yang dijanjikan.

## Pilihan pengguna

- GPT Codex; Windows; bahasa dokumentasi/laporan Indonesia, identifier kode Inggris.
- Stack tetap: Python, PostgreSQL, Redis opsional, Birdeye, GoPlus, Jupiter, Solana RPC, Telegram, LLM API opsional tahap lanjut.
- Telegram dahulu; dashboard web di luar scope saat ini.
- Satu subtugas per siklus; sempurnakan berdasarkan acceptance criteria, bukan refactor tanpa akhir.
- Commit dan push otomatis ke branch tugas setelah gate lulus dan remote tersedia. Merge tidak otomatis.
- Perubahan perilaku atau penghapusan fitur lama dibahas dahulu.
- Efisiensi token wajib, tanpa melewatkan pemeriksaan penting.

## Default yang dipilih

Nama repository: meme-ai-trader. Repository private. Mulai tanpa subscription baru: anggaran layanan berbayar awal Rp0, gunakan mock/data fixture untuk pengembangan dan akses resmi gratis bila benar-benar memadai. Ini batas pembelian awal, bukan klaim seluruh sistem produksi dapat gratis. Jika fitur membutuhkan paket berbayar, laporkan kebutuhan dan tunggu penetapan anggaran; jangan mengganti sumber/data secara diam-diam.

Gunakan Python lokal di virtual environment Windows. PostgreSQL dipilih untuk database aplikasi; cara instalasi ditentukan setelah inspeksi lingkungan. Docker/WSL tidak wajib. Redis ditambahkan hanya jika ada kebutuhan yang dibuktikan.

## Belum ditetapkan

API/paket yang dimiliki, source repository, remote URL, modal live, universe token, horizon holding, batas risiko, slippage, dan ukuran sampel efektif belum diketahui. Jangan menganggap source code tidak ada sebelum memeriksa folder kerja. Parameter trading boleh dirancang sebagai hipotesis eksperimen, diberi versi dan diuji; tidak menjadi default live secara otomatis.

## Batas produk

Pengguna tunggal, wallet trading khusus saat live, tidak ada layanan kustodian pengguna lain. LLM tidak mempunyai akses signer. Tahap awal mengumpulkan data; paper dan backtest memakai executor simulasi. Parameter dan gate live mengikuti BLUEPRINT.md bagian 4, 21, 25, dan 27.

## Preferensi checklist yang dikonfirmasi

Checklist Markdown + ringkasan chat, hierarki milestone/subtugas/pemeriksaan, diperbarui setelah tugas selesai/terhambat, AI menandai selesai bila kriteria/tes lulus, persentase berbasis jumlah subtugas, bukti tes/commit/push ringkas, regresi dibuka kembali dan diperbaiki sebelum lanjut, serta riwayat perubahan status dipertahankan.
