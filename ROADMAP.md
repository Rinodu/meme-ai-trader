# Roadmap implementasi

Status runtime awal: semua NOT_STARTED. M1.1 READY berarti boleh dikerjakan, bukan sudah berjalan. Kerjakan subtugas sesuai urutan nomor dalam tiap milestone; rinci acceptance criteria di CURRENT.md sebelum mulai.

| ID | Scope | Subtugas berurutan | Fitur | Gate selesai | Status |
| --- | --- | --- | --- | --- | --- |
| M1 | Scope dan konfigurasi | 1. Periksa lingkungan/repo; 2. Buat kerangka/config collect_only; 3. Uji config dan tutup gate | CFG-001 | Mode aman, invalid config ditolak, runtime/setup terdokumentasi | DONE |
| M2 | Database dan collector | 1. Schema/raw repository; 2. Dedup/timestamps; 3. Adapter Birdeye; 4. Quality dan rekonsiliasi feed | DATA-001, DATA-002 | Data persisten, null/nol berbeda, kejadian terlambat/dobel diuji | NOT_STARTED |
| M3 | Discovery dan security | 1. Universe/filter; 2. Security adapter; 3. Gate UNKNOWN dan audit | DISC-001, SEC-001 | Kandidat dan penolakan tersimpan; data hilang tidak meloloskan entry | NOT_STARTED |
| M4 | Quant dan baseline | 1. Fitur/warm-up; 2. Sinyal/expiry; 3. Replay deterministik | STRAT-001 | Keputusan dapat diulang dengan input/config sama | NOT_STARTED |
| M5 | Risk dan exit | 1. Sizing/exposure; 2. Reservasi; 3. Exit/kill switch | RISK-001, RISK-002, EXIT-001 | Batas dan konkurensi diuji; pause mempertahankan exit | NOT_STARTED |
| M6 | Ledger dan simulator | 1. Intent/attempt; 2. State machine; 3. Restart/rekonsiliasi | EXEC-001, LEDGER-001 | Timeout/retry/restart tidak menggandakan order/fill | NOT_STARTED |
| M7 | Backtest dan label | 1. Replay waktu; 2. Cost model; 3. TP/SL/no-route labels | BT-001 | Tidak memakai future data; fill dan biaya eksplisit | NOT_STARTED |
| M8 | Validasi strategi | 1. Bekukan eksperimen; 2. Walk-forward/holdout; 3. Stress/report | EVAL-001 | Hasil dan ketidakpastian tercatat; boleh INCONCLUSIVE | NOT_STARTED |
| M9 | Telegram dan paper | 1. Allowlist/commands; 2. Approval TTL; 3. Forward paper | CTRL-001, PAPER-001 | Callback ganda aman; paper tidak punya jalur submit live | NOT_STARTED |
| M10 | Integrasi execution | 1. Quote/route; 2. Decode/simulation; 3. Signer boundary/status | QUOTE-001, SIGN-001 | Kontrak provider terverifikasi; tidak memerlukan trade mainnet untuk unit/integration fixture | NOT_STARTED |
| M11 | Live terbatas | 1. Gate/modal/policy; 2. Semi-auto diizinkan; 3. Rekonsiliasi actual fill | LIVE-001 | Aktivasi eksplisit, gate lulus, selisih paper/live dievaluasi | NOT_STARTED |
| M12 | Komponen tambahan | 1. On-chain lanjutan; 2. Anomaly ablation; 3. Social/LLM budget dan evaluasi | AI-001 | Tambahan dibanding baseline; biaya/manfaat dilaporkan | NOT_STARTED |
| M13 | Full automation | 1. Audit gate; 2. Recovery/runbook; 3. Aktivasi dan evaluasi | AUTO-001 | Semua gate relevan lulus; aktivasi eksplisit dan kontrol tetap tersedia | NOT_STARTED |

## Aturan transisi

Prasyarat default adalah milestone sebelumnya selesai; satu tugas tidak menyelesaikan seluruh milestone. Status: NOT_STARTED, IN_PROGRESS, BLOCKED, DONE; untuk hasil strategi gunakan PASS/FAIL/INCONCLUSIVE terpisah. Kemajuan ditentukan bukti, bukan jumlah file.

"Sempurnakan" berarti acceptance criteria terpenuhi, tes wajib lulus, dan tidak ada masalah kritis yang diketahui dalam lingkup. Peningkatan opsional masuk backlog, tidak memicu loop refactor tanpa akhir.

Jika strategi belum lolos M8, perbaiki hipotesis dan ulang validasi dengan periode yang sah; M9 paper dapat menjadi eksperimen lanjutan untuk mengumpulkan bukti bila dicatat eksplisit, tetapi tidak membuka gate live. Jika fitur tambahan M12 diperlukan untuk penelitian sebelum live, usulkan perubahan urutan dengan alasan; jangan memaksa M11 live hanya agar bisa meneliti M12.

Sumber gate rinci: BLUEPRINT.md bagian 21 dan 25. Parameter yang belum dibekukan atau hasil INCONCLUSIVE tidak boleh dianggap lolos live. Catat setiap penyesuaian roadmap; perubahan perilaku lama harus dibahas dahulu.

## Sumber progres

Status subtugas dan hitungan resmi berada di [PROGRESS.md](PROGRESS.md). Status milestone di tabel ini merupakan ringkasan yang disinkronkan saat subtugas/gate berubah. M1 selesai; M2.1 adalah tugas berikutnya. DIBUKA_KEMBALI pada checklist memerlukan penilaian ulang gate milestone terkait.
