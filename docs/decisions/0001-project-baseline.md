# ADR 0001 — Baseline proyek

Status: ACCEPTED untuk pilihan pengguna dan default perencanaan yang didelegasikan. Tanggal: 2026-09-15.

## Konteks

Edhu meminta target seluruh bot, dibangun bertahap, disempurnakan, lalu lanjut. Menggunakan GPT Codex di Windows, stack blueprint tetap, Telegram dahulu, satu subtugas, commit/push branch tugas, pembahasan sebelum perubahan perilaku lama, dan efisiensi token.

## Keputusan

Aplikasi modular Python, PostgreSQL, Redis opsional. Mulai collect_only. Blueprint v2 menjadi acuan teknis; PRD menyimpan pilihan produk. Dokumen kendali terpisah sesuai fungsi dengan pintu masuk konteks pendek. Semua fitur runtime awalnya PLANNED.

Default yang dipilih karena didelegasikan: nama meme-ai-trader, repo private, bahasa dokumen Indonesia/kode Inggris, tanpa pembelian subscription baru pada awal pengembangan. Modal dan parameter live tetap belum ditetapkan karena membutuhkan keputusan dan validasi nyata.

## Konsekuensi

Paket tidak mengasumsikan repo, tool, atau API sudah tersedia. Beberapa milestone bisa terhambat akses data/anggaran dan harus dilaporkan. Tidak ada dashboard atau aktivasi live otomatis. Perubahan arsitektur besar dicatat dalam ADR baru; perubahan perilaku lama dibahas dahulu.
