# Kontrak fitur

Semua PLANNED; path tes dan implementasi diisi setelah benar-benar tersedia. ID tetap stabil. Sebelum perubahan, petakan pemanggil/fitur terdampak. Perubahan perilaku atau penghapusan memerlukan pembahasan pengguna dahulu.

| ID | Tahap | Perilaku wajib | Status | Implementasi / bukti tes |
| --- | --- | --- | --- | --- |
| CFG-001 | M1 | Default collect_only; mode tidak didukung ditolak; credential hanya wajib pada fitur aktif | VERIFIED | `meme_ai_trader/config.py`; `tests/test_config.py` (5 tes lulus pada Python 3.11/3.12); matriks startup M1.3 lulus |
| DATA-001 | M2 | Event yang sama tidak tersimpan dua kali | PLANNED | Belum tersedia |
| DATA-002 | M2 | event_time dan received_at dipisah; null tidak disamakan nol | IN_PROGRESS | Schema/repository `raw_events`; round-trip PostgreSQL M2.1 membuktikan timestamp terpisah serta null/nol; perilaku event terlambat dilanjutkan M2.2 |
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
| CTRL-001 | M9 | Allowlist, approval sekali pakai, TTL, dan requote/risk ulang | PLANNED | Belum tersedia |
| PAPER-001 | M9 | Executor paper tidak menandatangani/mengirim transaksi live | PLANNED | Belum tersedia |
| QUOTE-001 | M10 | Ukuran/umur quote, min output dan kapasitas exit diperiksa | PLANNED | Belum tersedia |
| SIGN-001 | M10 | Signer terbatas; LLM tidak mengakses private key | PLANNED | Belum tersedia |
| LIVE-001 | M11 | Aktivasi eksplisit dan gate lengkap; biaya/fill aktual tercatat | PLANNED | Belum tersedia |
| AI-001 | M12 | Schema/cache/budget LLM; exit tidak bergantung jawaban LLM | PLANNED | Belum tersedia |
| AUTO-001 | M13 | Kontrol, rekonsiliasi, recovery, dan penghentian tetap aktif | PLANNED | Belum tersedia |

Status berikutnya: IN_PROGRESS, VERIFIED, BLOCKED; DEPRECATED hanya setelah keputusan eksplisit dan rencana migrasi. VERIFIED mensyaratkan kode serta tes relevan lulus; catat commit atau lokasi bukti. Jangan mengubah PLANNED menjadi VERIFIED berdasarkan dokumen desain.

Jika fitur VERIFIED mengalami regresi, gunakan status REOPENED dan tautkan ID subtugas DIBUKA_KEMBALI di PROGRESS.md. Perbaiki sebelum pekerjaan fitur baru; VERIFIED hanya dikembalikan setelah pemeriksaan relevan lulus.
