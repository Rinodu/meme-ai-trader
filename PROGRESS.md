# Checklist progres proyek

Versi checklist: 1.0. Kondisi awal: belum ada subtugas implementasi yang selesai. Dokumen telah disiapkan; hal itu tidak dihitung sebagai implementasi bot.

## Ringkasan

- Progres implementasi: **4/40 subtugas = 10,0%**.
- Milestone selesai: **1/13**.
- Tugas berikut: M2.2, dedup/timestamps Signal Bot.
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

Status milestone: DIKERJAKAN. Progres: 1/4 (25,0%). Gate: BELUM_DIPERIKSA.

- [x] **M2.1 — Schema/raw repository** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: raw repository integration; suite 55/55; detail `docs/tasks/CURRENT.md`.

- [ ] **M2.2 — Dedup/timestamps** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M2.3 — Adapter Birdeye** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M2.4 — Quality dan rekonsiliasi feed** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Data persisten, null/nol berbeda, kejadian terlambat/dobel diuji. Bukti gate: belum.

### M3 — Discovery dan security

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M3.1 — Universe/filter** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M3.2 — Security adapter** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M3.3 — Gate UNKNOWN dan audit** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Kandidat dan penolakan tersimpan; data hilang tidak meloloskan entry. Bukti gate: belum.

### M4 — Quant dan baseline

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M4.1 — Fitur/warm-up** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M4.2 — Sinyal/expiry** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M4.3 — Replay deterministik** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Keputusan dapat diulang dengan input/config sama. Bukti gate: belum.

### M5 — Risk dan exit

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M5.1 — Sizing/exposure** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M5.2 — Reservasi** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M5.3 — Exit/kill switch** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Batas dan konkurensi diuji; pause mempertahankan exit. Bukti gate: belum.

### M6 — Ledger dan simulator

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M6.1 — Intent/attempt** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M6.2 — State machine** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M6.3 — Restart/rekonsiliasi** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Timeout/retry/restart tidak menggandakan order/fill. Bukti gate: belum.

### M7 — Backtest dan label

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M7.1 — Replay waktu** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M7.2 — Cost model** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M7.3 — TP/SL/no-route labels** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Tidak memakai future data; fill dan biaya eksplisit. Bukti gate: belum.

### M8 — Validasi strategi

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M8.1 — Bekukan eksperimen** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M8.2 — Walk-forward/holdout** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M8.3 — Stress/report** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Hasil dan ketidakpastian tercatat; boleh INCONCLUSIVE. Bukti gate: belum.

### M9 — Telegram signal dan paper

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M9.1 — Allowlist/commands** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M9.2 — Signal dan update exit** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M9.3 — Forward paper** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Pesan dapat diaudit; tidak ada approval/submit transaksi. Bukti gate: belum.

### M10 — Simulator quote/biaya

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M10.1 — Quote/route** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M10.2 — Simulasi kapasitas/biaya** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M10.3 — Guard no-execution** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

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
