# Checklist progres proyek

Versi checklist: 1.0. Kondisi awal: belum ada subtugas implementasi yang selesai. Dokumen telah disiapkan; hal itu tidak dihitung sebagai implementasi bot.

## Ringkasan

- Progres implementasi: **3/40 subtugas = 7,5%**.
- Milestone selesai: **1/13**.
- Tugas berikut: M2.1, schema/raw repository.
- Hambatan yang diketahui: PostgreSQL belum tersedia tetapi baru dibutuhkan pada M2.
- Tes: gate M1 lulus pada Python 3.11/3.12; mode aman/invalid, credential aktif, secret redaction, diagnostics, dan setup diverifikasi. Branch M1.3: `task/m1-3-config-gate`.

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

AI boleh menetapkan SELESAI berdasarkan bukti tanpa meminta persetujuan rutin. Perubahan perilaku/penghapusan fitur lama dan aktivasi live tetap mengikuti aturan persetujuan proyek. Pemeriksaan yang tidak relevan boleh N/A disertai alasan; pemeriksaan wajib yang tidak bisa dijalankan adalah TERHAMBAT, bukan N/A.

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

Status milestone: DONE. Progres: 3/3 (100,0%). Gate: LULUS.

- [x] **M1.1 — Periksa lingkungan/repo** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus atau N/A beralasan.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: inspeksi source/Git/Python/infrastruktur 2026-09-15; tes aplikasi N/A; commit `84c944b` dan push berhasil pada `task/m1-1-project-config`; detail `docs/tasks/M1.1.md`.

- [x] **M1.2 — Buat kerangka/config collect_only** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus atau N/A beralasan.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: 5 tes lulus pada Python 3.11/3.12; startup default sukses dan mode invalid ditolak; commit `2b34cd2` dan push berhasil pada `task/m1-2-config`; detail `docs/tasks/M1.2.md`.

- [x] **M1.3 — Uji config dan tutup gate** — SELESAI
  - [x] Acceptance criteria di catatan tugas terpenuhi.
  - [x] Pemeriksaan relevan lulus atau N/A beralasan.
  - [x] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [x] Dokumentasi/status dan bukti diperbarui.
  - Bukti: matriks startup/config lulus; 5 tes pada Python 3.11/3.12; diagnostics dan tautan Markdown bersih; commit/push dilaporkan setelah finalisasi; detail `docs/tasks/CURRENT.md`.

Gate milestone: Mode aman, invalid config ditolak, runtime/setup terdokumentasi. Bukti gate: LULUS pada audit M1.3.

### M2 — Database dan collector

Status milestone: BELUM_MULAI. Progres: 0/4 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M2.1 — Schema/raw repository** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

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

### M9 — Telegram dan paper

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M9.1 — Allowlist/commands** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M9.2 — Approval TTL** — BELUM_MULAI
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

Gate milestone: Callback ganda aman; paper tidak punya jalur submit live. Bukti gate: belum.

### M10 — Integrasi execution

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M10.1 — Quote/route** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M10.2 — Decode/simulation** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M10.3 — Signer boundary/status** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Kontrak provider terverifikasi; tidak memerlukan trade mainnet untuk unit/integration fixture. Bukti gate: belum.

### M11 — Live terbatas

Status milestone: BELUM_MULAI. Progres: 0/3 (0,0%). Gate: BELUM_DIPERIKSA.

- [ ] **M11.1 — Gate/modal/policy** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M11.2 — Semi-auto diizinkan** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

- [ ] **M11.3 — Rekonsiliasi actual fill** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Aktivasi eksplisit, gate lulus, selisih paper/live dievaluasi. Bukti gate: belum.

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

### M13 — Full automation

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

- [ ] **M13.3 — Aktivasi dan evaluasi** — BELUM_MULAI
  - [ ] Acceptance criteria di catatan tugas terpenuhi.
  - [ ] Pemeriksaan relevan lulus atau N/A beralasan.
  - [ ] Fitur lama terdampak diperiksa; tidak ada regresi terbuka.
  - [ ] Dokumentasi/status dan bukti diperbarui.
  - Bukti: Tes belum; commit belum; push belum.

Gate milestone: Semua gate relevan lulus; aktivasi eksplisit dan kontrol tetap tersedia. Bukti gate: belum.

## Riwayat perubahan status

Satu baris per transisi bermakna; log lengkap tetap di catatan tugas. Jangan mencatat setiap tool call. Jika panjang, pindahkan baris lama ke arsip progres dan tautkan dari sini.

| Tanggal | ID | Dari → Ke | Alasan/bukti | Dampak hitungan |
| --- | --- | --- | --- | --- |
| 2026-09-15 | INIT | — → BELUM_MULAI | Checklist dibuat dari roadmap; belum ada kode terverifikasi | 0/40 = 0,0% |
| 2026-09-15 | M1.1 | BELUM_MULAI → SELESAI | Source hanya dokumen; Python/Git diperiksa; repo dan branch tugas dibuat; commit/push tertunda | 1/40 = 2,5% |
| 2026-09-15 | M1.2 | BELUM_MULAI → SELESAI | Kerangka/config aman dibuat; 5 tes lulus pada Python 3.11/3.12; startup terverifikasi | 2/40 = 5,0% |
| 2026-09-15 | M1.3 | BELUM_MULAI → SELESAI | Matriks config/startup, diagnostics, secret redaction, setup, dan dokumentasi lulus | 3/40 = 7,5% |
