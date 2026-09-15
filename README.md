# Meme AI Trader

Versi paket: 1.1, 15 September 2026. Pemilik: Edhu.

Target: bot Solana hingga full automation melalui milestone berurutan. Saat ini baru tersedia kerangka konfigurasi aman; belum ada collector, strategi, database, atau jalur transaksi.

## Mulai

1. Gunakan Python 3.11 atau lebih baru.
2. Jalankan `py -m meme_ai_trader`; tanpa konfigurasi tambahan aplikasi hanya memulai mode `collect_only`.
3. Jalankan tes dengan `py -m unittest discover -s tests -v`.
4. Atur environment lokal hanya saat fiturnya diperlukan; jangan commit file `.env`.
5. Gunakan prompt lanjutan di [PROMPTS.md](PROMPTS.md) untuk mengerjakan satu subtugas berikutnya.

Jika sudah ada repository, bandingkan dokumen ini dengan dokumen yang ada sebelum menyalin. Jangan menimpa aturan atau source code yang belum diperiksa.

## Peta dokumen

| Dokumen | Sumber kebenaran untuk |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Aturan kerja AI dan efisiensi konteks |
| [PRD.md](PRD.md) | Target produk dan pilihan pengguna |
| [BLUEPRINT.md](BLUEPRINT.md) | Rancangan teknis lengkap v2 |
| [ROADMAP.md](ROADMAP.md) | Urutan pekerjaan dan status milestone |
| [PROGRESS.md](PROGRESS.md) | Checklist bertingkat, persentase, bukti, dan riwayat |
| [docs/tasks/TEMPLATE.md](docs/tasks/TEMPLATE.md) | Form tugas dan pemeriksaan hasil |
| [FEATURES.md](FEATURES.md) | Kontrak perilaku dan bukti implementasi |
| [AI_CONTEXT.md](AI_CONTEXT.md) | Kondisi aktual dan serah terima sesi |
| [CHANGELOG.md](CHANGELOG.md) | Perubahan selesai |
| [TESTING.md](TESTING.md) | Pemeriksaan wajib sesuai dampak |
| [GIT_WORKFLOW.md](GIT_WORKFLOW.md) | Branch, commit, push, merge, pemulihan |
| [TOKEN_POLICY.md](TOKEN_POLICY.md) | Anggaran konteks coding dan LLM bot |
| [CREDENTIALS.md](CREDENTIALS.md) | Kebutuhan kredensial bertahap |
| [PROMPTS.md](PROMPTS.md) | Perintah untuk memulai dan melanjutkan |
| [docs/tasks/CURRENT.md](docs/tasks/CURRENT.md) | Kontrak satu tugas aktif |
| [docs/decisions/0001-project-baseline.md](docs/decisions/0001-project-baseline.md) | Keputusan awal |

Dokumen tidak menjamin fitur selalu utuh. Git, tes regresi, validasi runtime, dan review perubahan harus benar-benar diterapkan. Tidak ada tes aplikasi yang telah dijalankan hanya karena skenario tes tertulis dalam paket.
