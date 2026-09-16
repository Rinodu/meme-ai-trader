# Roadmap implementasi

Status runtime: M1.1 DONE; subtugas berikut dikerjakan berurutan. Rinci acceptance criteria di CURRENT.md sebelum mulai.

| ID | Scope | Subtugas berurutan | Fitur | Gate selesai | Status |
| --- | --- | --- | --- | --- | --- |
| M1 | Scope dan konfigurasi | 1. Periksa lingkungan/repo; 2. Buat kerangka/config Signal Bot; 3. Uji config dan tutup gate | CFG-001 | Mode aman, invalid config ditolak, runtime/setup terdokumentasi | DONE |
| M2 | Database dan collector | 1. Schema/raw repository; 2. Dedup/timestamps; 3. Adapter Birdeye; 4. Quality dan rekonsiliasi feed | DATA-001, DATA-002 | Data persisten, null/nol berbeda, kejadian terlambat/dobel diuji | DONE |
| M3 | Discovery dan security | 1. Universe/filter; 2. Security adapter; 3. Gate UNKNOWN dan audit | DISC-001, SEC-001 | Kandidat dan penolakan tersimpan; data hilang tidak meloloskan entry | DONE |
| M4 | Quant dan baseline | 1. Fitur/warm-up; 2. Sinyal/expiry; 3. Replay deterministik | STRAT-001 | Keputusan dapat diulang dengan input/config sama | DONE |
| M5 | Risk dan exit | 1. Sizing/exposure; 2. Reservasi; 3. Exit/kill switch | RISK-001, RISK-002, EXIT-001 | Batas dan konkurensi diuji; pause mempertahankan exit | DONE |
| M6 | Ledger dan simulator | 1. Intent/attempt; 2. State machine; 3. Restart/rekonsiliasi | EXEC-001, LEDGER-001 | Timeout/retry/restart tidak menggandakan order/fill | DONE |
| M7 | Backtest dan label | 1. Replay waktu; 2. Cost model; 3. TP/SL/no-route labels | BT-001 | Tidak memakai future data; fill dan biaya eksplisit | IN_PROGRESS (M7.1 done) |
| M8 | Validasi strategi | 1. Bekukan eksperimen; 2. Walk-forward/holdout; 3. Stress/report | EVAL-001 | Hasil dan ketidakpastian tercatat; boleh INCONCLUSIVE | NOT_STARTED |
| M9 | Telegram signal dan paper | 1. Telegram pribadi/allowlist; 2. Signal + exit update; 3. Forward paper signal | CTRL-001, PAPER-001, SIGNAL-001 | Pesan dapat diaudit; tidak ada approval/submit transaksi | NOT_STARTED |
| M10 | Simulator quote/biaya | 1. Quote/route; 2. Simulasi kapasitas/biaya; 3. Guard no-execution | QUOTE-001, NOEXEC-001 | Kontrak provider terverifikasi; tidak ada signing/submit transaksi | NOT_STARTED |
| M11 | Evaluasi kualitas sinyal | 1. Outcome sinyal manual; 2. Deviasi paper; 3. Laporan kualitas | SIGNAL-002, PROB-001 | Hasil tidak dilebihkan; probabilitas hanya jika terkalibrasi | NOT_STARTED |
| M12 | Komponen tambahan | 1. On-chain lanjutan; 2. Anomaly ablation; 3. Social/LLM budget dan evaluasi | AI-001 | Tambahan dibanding baseline; biaya/manfaat dilaporkan | NOT_STARTED |
| M13 | Operasi signal bot | 1. Audit signal-only; 2. Recovery/runbook; 3. Monitoring produksi | OPS-001 | Sinyal/alert/recovery andal; tidak ada executor | NOT_STARTED |

## Aturan transisi

Prasyarat default adalah milestone sebelumnya selesai; satu tugas tidak menyelesaikan seluruh milestone. Status: NOT_STARTED, IN_PROGRESS, BLOCKED, DONE; untuk hasil strategi gunakan PASS/FAIL/INCONCLUSIVE terpisah. Kemajuan ditentukan bukti, bukan jumlah file.

"Sempurnakan" berarti acceptance criteria terpenuhi, tes wajib lulus, dan tidak ada masalah kritis yang diketahui dalam lingkup. Peningkatan opsional masuk backlog, tidak memicu loop refactor tanpa akhir.

Jika strategi belum lolos M8, perbaiki hipotesis dan ulang validasi dengan periode yang sah; M9 paper signal mengumpulkan bukti tambahan tetapi tidak mengubah status validasi tanpa evaluasi. M11 mengevaluasi hasil sinyal dan tidak membuka eksekusi transaksi.

Sumber gate rinci: SIGNAL_BOT_SCOPE.md dan bagian evaluasi BLUEPRINT.md yang relevan. Parameter yang belum dibekukan atau hasil INCONCLUSIVE tidak boleh dipresentasikan sebagai peluang atau rekomendasi kuat. Catat setiap penyesuaian roadmap; perubahan perilaku lama harus dibahas dahulu.

Audit 2026-09-16: source legacy dan 55 tes tersedia, tetapi belum dihitung selesai pada roadmap Signal Bot sampai setiap acceptance criterion dipetakan. Guard no-execution sudah terbukti pada `51113e9` dan mendukung M10.3; gate M10 tetap belum lulus karena kontrak provider simulator belum diverifikasi.

## Sumber progres

Status subtugas dan hitungan resmi berada di [PROGRESS.md](PROGRESS.md). Status milestone di tabel ini merupakan ringkasan yang disinkronkan saat subtugas/gate berubah. Semua subtugas awal belum selesai. DIBUKA_KEMBALI pada checklist memerlukan penilaian ulang gate milestone terkait.
