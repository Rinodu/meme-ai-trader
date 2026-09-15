# Kredensial dan tahapan

Dokumen ini menginventarisasi kebutuhan; schema autentikasi provider harus diverifikasi saat integrasi. API/paket milik pengguna belum diketahui. Jangan meminta pengguna menempelkan rahasia ke chat.

| Layanan | Kredensial/konfigurasi | Tahap |
| --- | --- | --- |
| Birdeye | API key sesuai kontrak provider | Collector asli M2 |
| Solana RPC | URL HTTP/WS; provider tertentu menyertakan key | Saat pembacaan on-chain dibutuhkan |
| GoPlus | Metode autentikasi yang tersedia untuk endpoint/paket; standard app key/secret atau token bila berlaku | M3 |
| PostgreSQL | Connection string/password lokal; instance PostgreSQL 18.6 tersedia, rahasia tetap lokal | M2 |
| Redis | URL/password bila dipakai | Berdasarkan kebutuhan |
| Telegram | Bot token + allowlist user/chat ID | M9 |
| Jupiter | API key sesuai versi API | M10; quote bisa lebih awal bila dibutuhkan |
| Signer/wallet | Referensi secret/keypair khusus, terpisah dari LLM | Penandatanganan saat tahap yang diizinkan |
| LLM | API key provider yang dipilih | M12 |
| Social | Bergantung sumber resmi yang dipilih | M12 |

M1 dan tes fixture dapat dikerjakan tanpa key. Paper tidak memerlukan private key trading. Membaca alamat wallet publik tidak memerlukan private key. Devnet keypair bukan keypair live. RPC publik tidak selalu memerlukan key tetapi mempunyai keterbatasan; jangan menganggapnya memadai untuk produksi tanpa pengukuran.

Simpan nilai rahasia di environment lokal/secret manager; `.env.example` hanya nama variabel. Jangan menyalin private key ke dalam contoh konfigurasi. Secret-bearing URL juga harus disensor di log. Credential coder untuk Git terpisah dari credential bot.

Template konfigurasi dibuat pada M1 sesuai kebutuhan aktual, dengan default collect_only. Jangan mewajibkan semua credential pada startup ketika fiturnya nonaktif. Detail integrasi teknis dirujuk dari BLUEPRINT.md bagian 26 dan diverifikasi saat implementasi.
