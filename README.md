# Meme AI Trader — Paket kendali proyek

Versi paket: 1.2, 15 September 2026. Pemilik: Edhu.

Target: Signal Bot Solana hingga operasi signal yang andal melalui milestone berurutan; buy/sell dilakukan manual oleh Edhu. Lingkungan pengguna: Windows; alat coding: GPT Codex; antarmuka awal: Telegram. Paket ini berisi dokumen, bukan aplikasi trading yang sudah berjalan.

## Mulai

1. Ekstrak folder `meme-ai-trader` ke lokasi kerja, misalnya `C:\Projects\meme-ai-trader`.
2. Buka folder tersebut di lingkungan kerja Codex yang dapat mengaksesnya.
3. Gunakan prompt pertama di [PROMPTS.md](PROMPTS.md).
4. Kerjakan satu subtugas, periksa hasil, sempurnakan sampai kriteria selesai terpenuhi, lalu lanjut setelah pengguna meminta subtugas berikutnya.
5. Simpan ke repository remote private yang dimiliki pengguna. URL remote dan autentikasi belum tersedia; Codex tidak boleh mengarang keduanya.

Jika sudah ada repository, bandingkan dokumen ini dengan dokumen yang ada sebelum menyalin. Jangan menimpa aturan atau source code yang belum diperiksa.

## Peta dokumen

| Dokumen | Sumber kebenaran untuk |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Aturan kerja AI dan efisiensi konteks |
| [PRD.md](PRD.md) | Target produk dan pilihan pengguna |
| [BLUEPRINT.md](BLUEPRINT.md) | Rancangan teknis lengkap v2 (dibatasi oleh scope signal) |
| [SIGNAL_BOT_SCOPE.md](SIGNAL_BOT_SCOPE.md) | Batas produk signal-only yang berlaku |
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
