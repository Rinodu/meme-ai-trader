# Kontrak fitur

| ID | Kontrak | Status | Bukti |
| --- | --- | --- | --- |
| CFG-001 | Default `collect_only`; mode tidak didukung ditolak; key hanya wajib saat Birdeye aktif. | VERIFIED | `tests/test_config.py` |
| DATA-001 | Event yang sama tidak tersimpan dua kali. | VERIFIED | Unique index + `tests/test_raw_events_integration.py` |
| DATA-002 | `event_time` dan `received_at` terpisah; nol tidak sama dengan data hilang. | VERIFIED | Repository raw event + tes M2.2/M2.3 |

Kontrak discovery, security, strategy, risk, dan execution masih PLANNED di `ROADMAP.md`.
