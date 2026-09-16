# Kontrak fitur

| ID | Kontrak | Status | Bukti |
| --- | --- | --- | --- |
| CFG-001 | Default `collect_only`; mode tidak didukung ditolak; key hanya wajib saat Birdeye aktif. | VERIFIED | `tests/test_config.py` |
| DATA-001 | Event yang sama tidak tersimpan dua kali. | VERIFIED | Unique index + repository PostgreSQL |
| DATA-002 | `event_time` dan `received_at` terpisah; nol tidak sama dengan data hilang; feed terbaru dinilai point-in-time. | VERIFIED | Tes M2.2–M2.4 |
| DISC-001 | Universe kandidat dievaluasi deterministik, point-in-time, dan alasan penolakan tersimpan. | VERIFIED | `tests/test_discovery.py` |
| SEC-001 | Security `UNKNOWN`/`REJECT` memblokir entry dan keputusan dapat diaudit. | VERIFIED | `tests/test_security.py`, `tests/test_entry_gate.py` |
| STRAT-001 | Fitur point-in-time/warm-up, signal expiry, dan replay deterministik. | VERIFIED | Tes M4.1–M4.3 |
| EXEC-001 | Intent/attempt ber-ID terpisah, lifecycle tervalidasi, dan pending work dapat dimuat ulang. | VERIFIED | `tests/test_raw_events_integration.py` |
| BACKTEST-001 | Replay deterministik menggunakan urutan ketersediaan data (`received_at`), termasuk input out-of-order. | VERIFIED | `tests/test_replay.py` |
| BACKTEST-002 | Biaya fee, slippage, dan impact dihitung dari parameter basis point eksplisit. | VERIFIED | `tests/test_costs.py` |
| BACKTEST-003 | Label TP/SL/time-out dan status route/data tidak tersedia bersifat eksplisit. | VERIFIED | `tests/test_labels.py` |
| VALID-001 | Version dan parameter eksperimen memiliki fingerprint stabil. | VERIFIED | `tests/test_experiments.py` |
| VALID-002 | Split kronologis memisahkan development, validation, dan holdout. | VERIFIED | `tests/test_validation.py` |
| VALID-003 | Report metrik tidak mengklaim PASS tanpa threshold evaluasi. | VERIFIED | `tests/test_reporting.py` |

Kontrak backtest dan execution eksternal masih PLANNED di `ROADMAP.md`.
