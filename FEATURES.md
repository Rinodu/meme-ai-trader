# Kontrak fitur

| ID | Kontrak | Status | Bukti |
| --- | --- | --- | --- |
| CFG-001 | Default `collect_only`; mode tidak didukung ditolak; key hanya wajib saat Birdeye aktif. | VERIFIED | `tests/test_config.py` |
| DATA-001 | Event yang sama tidak tersimpan dua kali. | VERIFIED | Unique index + repository PostgreSQL |
| DATA-002 | `event_time` dan `received_at` terpisah; nol tidak sama dengan data hilang; feed terbaru dinilai point-in-time. | VERIFIED | Tes M2.2–M2.4 |
| DISC-001 | Universe kandidat dievaluasi deterministik, point-in-time, dan alasan penolakan tersimpan. | VERIFIED | `tests/test_discovery.py` |
| SEC-001 | Security `UNKNOWN`/`REJECT` memblokir entry dan keputusan dapat diaudit. | VERIFIED | `tests/test_security.py`, `tests/test_entry_gate.py` |
| STRAT-001 | Snapshot fitur point-in-time/warm-up dan signal threshold ber-expiry deterministik. | IN_PROGRESS | `tests/test_quant.py`, `tests/test_strategy.py` |

Kontrak strategy, risk, dan execution masih PLANNED di `ROADMAP.md`.
