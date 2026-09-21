# Checklist progres proyek

Versi checklist: 1.0. Kondisi awal: belum ada subtugas implementasi yang selesai. Dokumen telah disiapkan; hal itu tidak dihitung sebagai implementasi bot.

## Ringkasan

- Progres implementasi: **31/40 subtugas = 77,5%**.
- Milestone selesai: **9/13**.
- Tugas berikut: M11.1, outcome sinyal manual.
- Hambatan yang diketahui: acceptance scope baru belum memetakan source legacy secara per-subtugas.
- Audit source: 55 tes lulus pada PostgreSQL lokal; guard no-execution `51113e9` dipush. Ini belum mengubah hitungan 0/40 tanpa resertifikasi acceptance tiap subtugas.

## Cara menggunakan

Checklist ini sumber kebenaran status subtugas dan hitungan progres. ROADMAP.md tetap menyimpan urutan/ketergantungan, FEATURES.md menyimpan kontrak perilaku, CURRENT.md menyimpan lingkup dan bukti detail. Jangan menyalin log panjang ke sini.

Perbarui setelah satu subtugas selesai atau terhambat, serta saat menemukan regresi. Pada awal pengerjaan cukup ubah status tugas aktif menjadi DIKERJAKAN. Di akhir respons, tampilkan ringkasan checklist di chat. Tidak perlu memperbarui setelah setiap perintah kecil.

| Status | Arti | Kotak subtugas |
| --- | --- | --- |
| BELUM_MULAI | Belum diimplementasikan | [ ] |
| DIKERJAKAN | Sedang dikerjakan, kriteria belum lengkap | [ ] |
| TERHAMBAT | Ada prasyarat/gate wajib yang belum bisa dipenuhi | [ ] |
| SIAP_DIPERIKSA | Implementasi siap, pemeriksaan belum selesai | [ ] |
| SELESAI | Kriteria dan pemeriksaan wajib lulus dengan bukti | [x] |
| DIBUKA_KEMBALI | Sebelumnya selesai, kemudian terbukti rusak/tidak memenuhi kontrak | [ ] |

AI boleh menetapkan SELESAI berdasarkan bukti tanpa meminta persetujuan rutin. Perubahan perilaku/penghapusan fitur lama tetap mengikuti aturan persetujuan proyek. Eksekusi trading live berada di luar scope signal bot. Pemeriksaan yang tidak relevan boleh N/A disertai alasan; pemeriksaan wajib yang tidak bisa dijalankan adalah TERHAMBAT, bukan N/A.

## Perhitungan dan konsistensi

Persentase proyek = jumlah subtugas SELESAI dibagi seluruh subtugas implementasi yang terdaftar, dikali 100. Setiap subtugas berbobot satu. Bulatkan satu angka desimal. Persentase menunjukkan jumlah pekerjaan, bukan waktu, kualitas strategi, atau kesiapan live.

- Hitung hanya kotak subtugas dengan ID Mx.y; jangan menghitung checkbox pemeriksaan atau milestone dua kali.
- Tugas DIKERJAKAN/TERHAMBAT tidak mendapat kredit parsial. DIBUKA_KEMBALI mengurangi pembilang.
- Milestone selesai bila seluruh subtugasnya selesai dan gate milestone lulus. Gate adalah syarat, bukan unit tambahan dalam denominator. Tampilkan status gate terpisah jika semua tugas selesai tetapi gate belum lulus.
- Jika scope bertambah/dipecah, catat alasan, jumlah lama/baru, dan persentase sebelum/sesudah di riwayat. Jangan memecah pekerjaan untuk mempercantik persentase.
- Tugas yang dibatalkan tidak boleh ditandai selesai; keluarkan dari scope aktif hanya melalui keputusan scope yang dicatat, sambil mempertahankan rekam ID-nya.
- Saat regresi ditemukan, buka kembali tugas asal dan fitur terdampak, hitung ulang progres, dan perbaiki sebelum melanjutkan fitur baru. Periksa milestone turunan; tandai gate yang tidak lagi valid. Jangan otomatis menghapus hasil semua tugas turunan tanpa penilaian dampak.
- Setelah perbaikan, lakukan tes regresi relevan sebelum mengembalikan status SELESAI.

## Bukti ringkas

Pada setiap tugas gunakan: `Tes: perintah/hasil atau rujukan bukti; Commit implementasi: SHA atau belum; Push: berhasil/tertunda/gagal/tidak relevan + branch; Detail: lokasi catatan tugas`.

Status push dilaporkan terpisah dari kelulusan fungsional. Tugas kode yang teruji dapat selesai lokal meski push terhambat, kecuali acceptance criteria tugas itu memang mensyaratkan push; tulis BELUM_TERSIMPAN_REMOTE dengan jelas. Jangan mengklaim remote backup telah tersedia.

Hindari lingkaran commit: dokumen tidak perlu mencantumkan SHA commit yang memuat dirinya. Gunakan SHA implementasi yang sudah ada; catatan final/hasil push boleh disimpan pada commit dokumentasi berikutnya atau pembaruan berikutnya. Jangan melakukan commit berulang hanya untuk memperbarui SHA sendiri. Laporkan hasil push aktual di chat setelah tool mengonfirmasi.

## Form per milestone

### M1 — Scope dan konfigurasi

Status milestone: SELESAI. Progres: 3/3 (100%). Gate: LULUS.

- [x] **M1.1 — Periksa lingkungan/repo** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: config 5/5; suite 55/55; `51113e9`; detail `docs/tasks/CURRENT.md`.

- [x] **M1.2 — Buat kerangka/config Signal Bot** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: config 5/5; smoke test 3 mode; detail `docs/tasks/CURRENT.md`.

- [x] **M1.3 — Uji config dan tutup gate** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: suite 55/55; guard no-execution; detail `docs/tasks/CURRENT.md`.

Gate milestone: Mode aman, invalid config ditolak, runtime/setup terdokumentasi. Bukti gate: belum.

### M2 — Database dan collector

Status milestone: SELESAI. Progres: 4/4 (100%). Gate: LULUS.

- [x] **M2.1 — Schema/raw repository** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: raw repository integration; suite 55/55; detail `docs/tasks/CURRENT.md`.

- [x] **M2.2 — Dedup/timestamps** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: integration 12/12 PostgreSQL; detail `docs/tasks/CURRENT.md`.

- [x] **M2.3 — Adapter Birdeye** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: adapter HTTP GET dan raw snapshot aman; Birdeye + raw-event integration 15/15 PostgreSQL; detail `docs/tasks/CURRENT.md`.

- [x] **M2.4 — Quality dan rekonsiliasi feed** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: quality/reconciliation membaca event tersedia terbaru; feed + Birdeye + raw-event integration 17/17 PostgreSQL; detail `docs/tasks/CURRENT.md`.

Gate milestone: Data persisten, null/nol berbeda, kejadian terlambat/dobel diuji. Bukti gate: M2.4 17/17 PostgreSQL.

### M3 — Discovery dan security

Status milestone: SELESAI. Progres: 3/3 (100%). Gate: LULUS.

- [x] **M3.1 — Universe/filter** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: filter kandidat point-in-time; discovery + feed 5/5; detail `docs/tasks/CURRENT.md`.

- [x] **M3.2 — Security adapter** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: security fail-closed PASS/REJECT/UNKNOWN; security + discovery + feed 9/9; detail `docs/tasks/CURRENT.md`.

- [x] **M3.3 — Gate UNKNOWN dan audit** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: entry gate fail-closed dan audit immutable; entry-gate + security + discovery + feed 12/12; detail `docs/tasks/CURRENT.md`.

Gate milestone: Kandidat dan penolakan tersimpan; data hilang tidak meloloskan entry. Bukti gate: belum.

### M4 — Quant dan baseline

Status milestone: SELESAI. Progres: 3/3 (100%). Gate: LULUS.

- [x] **M4.1 — Fitur/warm-up** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: quant + raw-event integration 15/15 PostgreSQL; detail `docs/tasks/CURRENT.md`.

- [x] **M4.2 — Sinyal/expiry** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: strategy + quant + no-execution 8/8; detail `docs/tasks/CURRENT.md`.

- [x] **M4.3 — Replay deterministik** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: replay + strategy + quant + no-execution 10/10; detail `docs/tasks/CURRENT.md`.

Gate milestone: Keputusan dapat diulang dengan input/config sama. Bukti gate: belum.

### M5 — Risk dan exit

Status milestone: SELESAI. Progres: 3/3 (100%). Gate: LULUS.

- [x] **M5.1 — Sizing/exposure** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: risk simulator + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

- [x] **M5.2 — Reservasi** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: reservation atomik/idempoten + no-execution 14/14 PostgreSQL; detail `docs/tasks/CURRENT.md`.

- [x] **M5.3 — Exit/kill switch** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: control legacy simulator + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

Gate milestone: Batas dan konkurensi diuji; pause mempertahankan exit. Bukti gate: belum.

### M6 — Ledger dan simulator

Status milestone: SELESAI. Progres: 3/3 (100%). Gate: LULUS.

- [x] **M6.1 — Intent/attempt** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: ledger simulator + no-execution 14/14 PostgreSQL; detail `docs/tasks/CURRENT.md`.

- [x] **M6.2 — State machine** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: lifecycle ledger simulator + no-execution 14/14 PostgreSQL; detail `docs/tasks/CURRENT.md`.

- [x] **M6.3 — Restart/rekonsiliasi** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: restart/reconciliation simulator + no-execution 14/14 PostgreSQL; detail `docs/tasks/CURRENT.md`.

Gate milestone: Timeout/retry/restart tidak menggandakan order/fill. Bukti gate: belum.

### M7 — Backtest dan label

Status milestone: SELESAI. Progres: 3/3 (100%). Gate: LULUS.

- [x] **M7.1 — Replay waktu** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: replay + quant + strategy + no-execution 10/10; detail `docs/tasks/CURRENT.md`.

- [x] **M7.2 — Cost model** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: cost model simulator + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

- [x] **M7.3 — TP/SL/no-route labels** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: label outcome simulator + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

Gate milestone: Tidak memakai future data; fill dan biaya eksplisit. Bukti gate: belum.

### M8 — Validasi strategi

Status milestone: SELESAI. Progres: 3/3 (100%). Gate: LULUS.

- [x] **M8.1 — Bekukan eksperimen** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: fingerprint eksperimen + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

- [x] **M8.2 — Walk-forward/holdout** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: split holdout + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

- [x] **M8.3 — Stress/report** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: report inconclusive + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

Gate milestone: Hasil dan ketidakpastian tercatat; boleh INCONCLUSIVE. Bukti gate: belum.

### M9 — Telegram signal dan paper

Status milestone: SELESAI. Progres: 3/3 (100%). Gate: LULUS.

- [x] **M9.1 — Allowlist/commands** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: allowlist Telegram dan penghapusan approval buy/sell; Telegram + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

- [x] **M9.2 — Signal dan update exit** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: formatter sinyal manual + Telegram + no-execution 4/4; detail `docs/tasks/CURRENT.md`.

- [x] **M9.3 — Forward paper** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: paper signal netral + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

Gate milestone: Pesan dapat diaudit; tidak ada approval/submit transaksi. Bukti gate: belum.

### M10 — Simulator quote/biaya

Status milestone: SELESAI. Progres: 3/3 (100%). Gate: LULUS.

- [x] **M10.1 — Quote/route** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: quote simulator + no-execution 3/3; detail `docs/tasks/CURRENT.md`.

- [x] **M10.2 — Simulasi kapasitas/biaya** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: payload simulation + quote + no-execution 4/4; detail `docs/tasks/CURRENT.md`.

- [x] **M10.3 — Guard no-execution** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: signer disabled + source guard 3/3; detail `docs/tasks/CURRENT.md`.

Gate milestone: Kontrak provider terverifikasi; tidak ada signing/submit transaksi. Bukti gate: belum.

### M11 — Evaluasi kualitas sinyal

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M11.1 — Outcome sinyal manual** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M11.2 — Deviasi paper** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M11.3 — Laporan kualitas** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Hasil tidak dilebihkan; probabilitas hanya jika terkalibrasi. Bukti gate: belum.

### M12 — Komponen tambahan

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M12.1 — On-chain lanjutan** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M12.2 — Anomaly ablation** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M12.3 — Social/LLM budget dan evaluasi** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Tambahan dibanding baseline; biaya/manfaat dilaporkan. Bukti gate: belum.

### M13 — Operasi signal bot

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M13.1 — Audit gate** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M13.2 — Recovery/runbook** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M13.3 — Monitoring produksi** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Sinyal/alert/recovery andal; tidak ada executor. Bukti gate: belum.

## Riwayat perubahan status

Satu baris per transisi bermakna; log lengkap tetap di catatan tugas. Jangan mencatat setiap tool call. Jika panjang, pindahkan baris lama ke arsip progres dan tautkan dari sini.

| Tanggal | ID | Dari → Ke | Alasan/bukti | Dampak hitungan |
| --- | --- | --- | --- | --- |
| 2026-09-15 | INIT | — → BELUM_MULAI | Checklist dibuat dari roadmap; belum ada kode terverifikasi | 0/40 = 0,0% |
| 2026-09-16 | SCOPE | Full automation → Signal Bot | Keputusan Edhu: Telegram pribadi, kandidat terbaik, buy/sell manual; simulator dipertahankan | 0/40 = 0,0% |
| 2026-09-16 | AUDIT | Dokumen paket → source terverifikasi | 55 tes lulus; guard no-execution dipush `51113e9`; legacy belum otomatis diresertifikasi | 0/40 = 0,0% |
| 2026-09-16 | M1.1 | BELUM_MULAI → SELESAI | Runtime/Git/Python/source diverifikasi; config 5/5 dan suite 55/55 | 1/40 = 2,5% |
| 2026-09-16 | M1.2 | BELUM_MULAI → SELESAI | Tiga mode Signal Bot dan startup diverifikasi | 2/40 = 5,0% |
| 2026-09-16 | M1.3 | BELUM_MULAI → SELESAI | Config gate dan guard no-execution lulus dalam suite 55/55 | 3/40 = 7,5% |
| 2026-09-16 | M2.1 | BELUM_MULAI → SELESAI | Schema/raw repository teruji di PostgreSQL lokal | 4/40 = 10,0% |
| 2026-09-16 | M2.2 | BELUM_MULAI → SELESAI | Dedup, UTC, dan late-event visibility lulus 12/12 | 5/40 = 12,5% |
| 2026-09-16 | M2.3 | BELUM_MULAI → SELESAI | Adapter Birdeye read-only dan raw snapshot lulus 15/15 | 6/40 = 15,0% |
| 2026-09-16 | M2.4 | BELUM_MULAI → SELESAI | Feed quality dan rekonsiliasi availability lulus 17/17 | 7/40 = 17,5% |
| 2026-09-16 | M3.1 | BELUM_MULAI → SELESAI | Filter universe point-in-time lulus 5/5 | 8/40 = 20,0% |
| 2026-09-16 | M3.2 | BELUM_MULAI → SELESAI | Security fail-closed lulus 9/9 | 9/40 = 22,5% |
| 2026-09-16 | M3.3 | BELUM_MULAI → SELESAI | Entry gate fail-closed lulus 12/12 | 10/40 = 25,0% |
| 2026-09-16 | M4.1 | BELUM_MULAI → SELESAI | Fitur/warm-up point-in-time lulus 15/15 | 11/40 = 27,5% |
| 2026-09-16 | M4.2 | BELUM_MULAI → SELESAI | Sinyal deterministik dan expiry lulus 8/8 | 12/40 = 30,0% |
| 2026-09-16 | M4.3 | BELUM_MULAI → SELESAI | Replay deterministik lulus 10/10 | 13/40 = 32,5% |
| 2026-09-16 | M5.1 | BELUM_MULAI → SELESAI | Sizing simulator dan no-execution lulus 3/3 | 14/40 = 35,0% |
| 2026-09-16 | M5.2 | BELUM_MULAI → SELESAI | Reservation simulator PostgreSQL lulus 14/14 | 15/40 = 37,5% |
| 2026-09-16 | M5.3 | BELUM_MULAI → SELESAI | Control simulator dan no-execution lulus 3/3 | 16/40 = 40,0% |
| 2026-09-16 | M6.1 | BELUM_MULAI → SELESAI | Ledger simulator dan no-execution lulus 14/14 | 17/40 = 42,5% |
| 2026-09-16 | M6.2 | BELUM_MULAI → SELESAI | State machine simulator lulus 14/14 | 18/40 = 45,0% |
| 2026-09-16 | M6.3 | BELUM_MULAI → SELESAI | Restart/reconciliation simulator lulus 14/14 | 19/40 = 47,5% |
| 2026-09-16 | M7.1 | BELUM_MULAI → SELESAI | Time replay lulus 10/10 | 20/40 = 50,0% |
| 2026-09-16 | M7.2 | BELUM_MULAI → SELESAI | Cost model simulator lulus 3/3 | 21/40 = 52,5% |
| 2026-09-16 | M7.3 | BELUM_MULAI → SELESAI | Label outcome simulator lulus 3/3 | 22/40 = 55,0% |
| 2026-09-16 | M8.1 | BELUM_MULAI → SELESAI | Fingerprint eksperimen lulus 3/3 | 23/40 = 57,5% |
| 2026-09-16 | M8.2 | BELUM_MULAI → SELESAI | Split holdout lulus 3/3 | 24/40 = 60,0% |
| 2026-09-16 | M8.3 | BELUM_MULAI → SELESAI | Report inconclusive lulus 3/3 | 25/40 = 62,5% |
