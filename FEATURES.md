# Kontrak fitur

Semua PLANNED; path tes dan implementasi diisi setelah benar-benar tersedia. ID tetap stabil. Sebelum perubahan, petakan pemanggil/fitur terdampak. Perubahan perilaku atau penghapusan memerlukan pembahasan pengguna dahulu.

| ID | Tahap | Perilaku wajib | Status | Implementasi / bukti tes |
| --- | --- | --- | --- | --- |
| CFG-001 | M1 | Default collect_only; mode tidak didukung ditolak; credential hanya wajib pada fitur aktif | VERIFIED | `tests/test_config.py`, `tests/test_no_execution.py`; suite 55/55 |
| DATA-001 | M2 | Event yang sama tidak tersimpan dua kali | PLANNED | Belum tersedia |
| DATA-002 | M2 | event_time dan received_at dipisah; null tidak disamakan nol | PLANNED | Belum tersedia |
| DISC-001 | M3 | Kandidat ditolak dan alasan tetap tersimpan | PLANNED | Belum tersedia |
| SEC-001 | M3 | UNKNOWN/REJECT memblokir entry | PLANNED | Belum tersedia |
| STRAT-001 | M4 | Input/config sama memberi keputusan sama; sinyal punya expiry | PLANNED | Belum tersedia |
| RISK-001 | M5 | Sizing, exposure, daily loss, dan fee reserve diterapkan | PLANNED | Belum tersedia |
| RISK-002 | M5 | Reservasi atomik mencegah dua order memakai modal sama | PLANNED | Belum tersedia |
| EXIT-001 | M5 | Pause entry tidak mematikan exit; no-route bukan fill sukses | PLANNED | Belum tersedia |
| EXEC-001 | M6 | Timeout/retry/restart tidak menciptakan order duplikat | PLANNED | Belum tersedia |
| LEDGER-001 | M6 | Saldo, fill, dan pending intent direkonsiliasi tanpa hitung ganda | PLANNED | Belum tersedia |
| BT-001 | M7 | Replay hanya memakai data tersedia; biaya dan label ambigu eksplisit | PLANNED | Belum tersedia |
| EVAL-001 | M8 | Holdout tidak digunakan menyetel parameter; ketidakpastian dilaporkan | PLANNED | Belum tersedia |
| CTRL-001 | M9 | Telegram pribadi/allowlist; command kontrol tidak dapat mengirim transaksi | PLANNED | Belum tersedia |
| PAPER-001 | M9 | Paper signal mencatat hasil simulasi tanpa signing/submission | PLANNED | Belum tersedia |
| QUOTE-001 | M10 | Simulator quote menilai ukuran/umur quote, biaya, dan kapasitas exit | PLANNED | Belum tersedia |
| NOEXEC-001 | M10 | Signal-only runtime tidak memiliki signing atau submission transaksi | VERIFIED | `tests/test_no_execution.py`; `51113e9` |
| SIGNAL-002 | M11 | Outcome sinyal dan kualitas exit dilaporkan tanpa mengklaim fill aktual | VERIFIED | `meme_ai_trader/paper_deviation.py`, `meme_ai_trader/quality_report.py`; tests M11.2/M11.3; merge `cd89804` |
| PROB-001 | M11 | Probabilitas hanya muncul setelah label, evaluasi out-of-sample, dan kalibrasi | VERIFIED | `meme_ai_trader/quality_report.py`; uncalibrated probability suppression test; merge `cd89804` |
| AI-001 | M12 | Schema/cache/budget LLM; exit tidak bergantung jawaban LLM | PLANNED | Belum tersedia |
| OPS-001 | M13 | Monitoring/recovery signal bot andal tanpa executor | PLANNED | Belum tersedia |
| SIGNAL-001 | M9 | Nol atau satu kandidat terbaik per siklus, dengan alasan entry/exit dan expiry | PLANNED | Belum tersedia |

Status berikutnya: IN_PROGRESS, VERIFIED, BLOCKED; DEPRECATED hanya setelah keputusan eksplisit dan rencana migrasi. VERIFIED mensyaratkan kode serta tes relevan lulus; catat commit atau lokasi bukti. Jangan mengubah PLANNED menjadi VERIFIED berdasarkan dokumen desain.

Jika fitur VERIFIED mengalami regresi, gunakan status REOPENED dan tautkan ID subtugas DIBUKA_KEMBALI di PROGRESS.md. Perbaiki sebelum pekerjaan fitur baru; VERIFIED hanya dikembalikan setelah pemeriksaan relevan lulus.
