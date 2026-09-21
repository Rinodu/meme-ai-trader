# Kontrak fitur

Semua PLANNED; path tes dan implementasi diisi setelah benar-benar tersedia. ID tetap stabil. Sebelum perubahan, petakan pemanggil/fitur terdampak. Perubahan perilaku atau penghapusan memerlukan pembahasan pengguna dahulu.

| ID | Tahap | Perilaku wajib | Status | Implementasi / bukti tes |
| --- | --- | --- | --- | --- |
| CFG-001 | M1 | Default collect_only; mode tidak didukung ditolak; credential hanya wajib pada fitur aktif | VERIFIED | `tests/test_config.py`, `tests/test_no_execution.py`; suite 55/55 |
| DATA-001 | M2 | Event yang sama tidak tersimpan dua kali | VERIFIED | `tests/test_raw_events_integration.py`; suite 106/106 |
| DATA-002 | M2 | event_time dan received_at dipisah; null tidak disamakan nol | VERIFIED | `tests/test_raw_events_integration.py`, `tests/test_birdeye.py`; suite 106/106 |
| DISC-001 | M3 | Kandidat ditolak dan alasan tetap tersimpan | VERIFIED | `tests/test_discovery.py`; suite 106/106 |
| SEC-001 | M3 | UNKNOWN/REJECT memblokir entry | VERIFIED | `tests/test_security.py`, `tests/test_entry_gate.py`; suite 106/106 |
| STRAT-001 | M4 | Input/config sama memberi keputusan sama; sinyal punya expiry | VERIFIED | `tests/test_strategy.py`, `tests/test_replay.py`; suite 106/106 |
| RISK-001 | M5 | Sizing, exposure, daily loss, dan fee reserve diterapkan | VERIFIED | `tests/test_risk.py`; suite 106/106 |
| RISK-002 | M5 | Reservasi atomik mencegah dua order memakai modal sama | VERIFIED | `tests/test_raw_events_integration.py`; suite 106/106 |
| EXIT-001 | M5 | Pause entry tidak mematikan exit; no-route bukan fill sukses | VERIFIED | `tests/test_controls.py`, `tests/test_labels.py`; suite 106/106 |
| EXEC-001 | M6 | Timeout/retry/restart tidak menciptakan order duplikat | VERIFIED | `tests/test_raw_events_integration.py`; suite 106/106 |
| LEDGER-001 | M6 | Saldo, fill, dan pending intent direkonsiliasi tanpa hitung ganda | VERIFIED | `tests/test_raw_events_integration.py`; suite 106/106 |
| BT-001 | M7 | Replay hanya memakai data tersedia; biaya dan label ambigu eksplisit | VERIFIED | `tests/test_replay.py`, `tests/test_costs.py`, `tests/test_labels.py`; suite 106/106 |
| EVAL-001 | M8 | Holdout tidak digunakan menyetel parameter; ketidakpastian dilaporkan | VERIFIED | `tests/test_validation.py`, `tests/test_reporting.py`, `tests/test_experiments.py`; suite 106/106 |
| CTRL-001 | M9 | Telegram pribadi/allowlist; command kontrol tidak dapat mengirim transaksi | VERIFIED | `tests/test_telegram.py`, `tests/test_signal_message.py`; suite 106/106 |
| PAPER-001 | M9 | Paper signal mencatat hasil simulasi tanpa signing/submission | VERIFIED | `tests/test_paper.py`, `tests/test_no_execution.py`; suite 106/106 |
| QUOTE-001 | M10 | Simulator quote menilai ukuran/umur quote, biaya, dan kapasitas exit | VERIFIED | `tests/test_quotes.py`, `tests/test_simulation.py`; suite 106/106 |
| NOEXEC-001 | M10 | Signal-only runtime tidak memiliki signing atau submission transaksi | VERIFIED | `tests/test_no_execution.py`; `51113e9` |
| SIGNAL-002 | M11 | Outcome sinyal dan kualitas exit dilaporkan tanpa mengklaim fill aktual | VERIFIED | `meme_ai_trader/paper_deviation.py`, `meme_ai_trader/quality_report.py`; tests M11.2/M11.3; merge `cd89804` |
| PROB-001 | M11 | Probabilitas hanya muncul setelah label, evaluasi out-of-sample, dan kalibrasi | VERIFIED | `meme_ai_trader/quality_report.py`; uncalibrated probability suppression test; merge `cd89804` |
| AI-001 | M12 | Schema/cache/budget LLM; exit tidak bergantung jawaban LLM | VERIFIED | M12.3 10/10; suite 106/106; merge `f451601`; detail `docs/tasks/M12.3.md` |
| OPS-001 | M13 | Monitoring/recovery signal bot andal tanpa executor | VERIFIED | `docs/tasks/M13.1.md`, `docs/tasks/M13.2.md`, `docs/tasks/M13.3.md`; M13 tests 15/15; suite 121/121; merge `6b91895` |
| SIGNAL-001 | M9 | Nol atau satu kandidat terbaik per siklus, dengan alasan entry/exit dan expiry | VERIFIED | `tests/test_signal_message.py`, `tests/test_strategy.py`; suite 106/106 |

Status berikutnya: IN_PROGRESS, VERIFIED, BLOCKED; DEPRECATED hanya setelah keputusan eksplisit dan rencana migrasi. VERIFIED mensyaratkan kode serta tes relevan lulus; catat commit atau lokasi bukti. Jangan mengubah PLANNED menjadi VERIFIED berdasarkan dokumen desain.

Jika fitur VERIFIED mengalami regresi, gunakan status REOPENED dan tautkan ID subtugas DIBUKA_KEMBALI di PROGRESS.md. Perbaiki sebelum pekerjaan fitur baru; VERIFIED hanya dikembalikan setelah pemeriksaan relevan lulus.
