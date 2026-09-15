# Strategi pengujian

Status awal: skenario berikut adalah persyaratan, belum tes yang telah lulus.

| Perubahan | Pemeriksaan minimum |
| --- | --- |
| Markdown | Referensi/struktur/status konsisten; tidak perlu seluruh tes aplikasi |
| Config | Mode default, nilai invalid, kredensial wajib hanya pada mode terkait, redaksi rahasia |
| Collector | Dedup, event terlambat, field hilang, nol vs null, timestamp, reconnect sesuai adapter |
| Security | PASS/REJECT/UNKNOWN; timeout tidak lolos entry |
| Risk/saldo | Nilai batas, reservasi atomik, dua intent bersamaan, daily loss, fee reserve |
| Executor | Timeout UNKNOWN, resend vs replacement, callback ganda, expiry, restart dan rekonsiliasi |
| Exit/control | Pause tidak mematikan monitor/exit; rute hilang bukan fill; tidak oversell |
| Database | Migrasi pada schema/data sebelumnya, constraint, backup/restore sesuai dampak |
| Strategi/label | Data point-in-time, warm-up, TP/SL intrabar ambigu, no route dan biaya |
| LLM | Schema, timeout/cache, input tidak tepercaya, budget dan fallback |

Mulai dari tes terarah. Jalankan regresi komponen yang bergantung pada kontrak yang berubah. Suite lintas modul dilakukan saat integrasi/milestone atau ketika dampak menyebar; tidak wajib diulang setelah edit typo.

Pisahkan fixture/mock, replay, provider read-only, dan live. Tes otomatis biasa tidak mengirim transaksi mainnet dan tidak memerlukan private key. Tes live bukan shortcut untuk membuktikan logic dasar.

Setiap hasil mencatat perintah, tanggal, status, cakupan dan commit bila tersedia. SKIPPED/BLOCKED tidak sama dengan PASS. Jangan membuat tes yang sekadar menyalin rumus implementasi; uji perilaku, kasus batas, kegagalan, dan invarian.

Pada kode yang sama, jangan mengulang suite yang sudah lulus tanpa alasan. Jika kode relevan berubah, bukti sebelumnya tidak lagi cukup. CI pada branch tugas dibangun ketika kerangka proyek tersedia; status wajibnya disesuaikan risiko, bukan diklaim sudah aktif dalam paket ini.

Hasil pemeriksaan harus dirujuk dari PROGRESS.md. Tes belum dijalankan tidak boleh dicentang lulus; N/A memerlukan alasan dan hanya berlaku untuk pemeriksaan yang memang tidak relevan. Regresi membuka kembali tugas/fitur sebelum melanjutkan pekerjaan baru.
