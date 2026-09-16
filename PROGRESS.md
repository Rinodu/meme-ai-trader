# Progress — source of truth status tugas

## Ringkasan
- Selesai: **20/40 = 50%**
- Milestone selesai: **5/13**
- Aktif/berikut: **M7.2 Cost model**
- Bukti terakhir: 42 tes Python 3.12/PostgreSQL lokal lulus.
- Hambatan: Pyright Serena belum mengikuti `.venv` untuk Psycopg; runtime/test lulus.

Status: `[x]=SELESAI`, `[~]=DIKERJAKAN`, `[ ]=BELUM_MULAI`, `[!]=TERHAMBAT`, `[R]=DIBUKA_KEMBALI`.
Satu task SELESAI hanya bila acceptance criteria + tes wajib punya bukti di `docs/tasks/`.

## Checklist
- M1 — Scope/config — **DONE; gate LULUS**
  - [x] M1.1 Periksa lingkungan/repo — `84c944b`
  - [x] M1.2 Kerangka/config `collect_only` — 5 tes; `2b34cd2`
  - [x] M1.3 Uji config/tutup gate — 5 tes; `ce9c273`
- M2 — Database/collector — **DONE; gate LULUS**
  - [x] M2.1 Schema/raw repository — 6 tes; `c27ec8e`
  - [x] M2.2 Dedup/timestamps — 9 tes total; detail `docs/tasks/CURRENT.md`
  - [x] M2.3 Adapter Birdeye — 13 tes; `ac17ca5`, `2d0dd33`
  - [x] M2.4 Quality/reconciliation feed — 17 tes; detail `docs/tasks/CURRENT.md`
- M3 — Discovery/security — **DONE; gate LULUS**
  - [x] M3.1 Universe/filter — `10b8669`
  - [x] M3.2 Security adapter — `263f024`
  - [x] M3.3 UNKNOWN gate/audit — `f580f90`; 27 tes
- M4 — Quant/baseline — **DONE; gate LULUS**
  - [x] M4.1 Features/warm-up; [x] M4.2 Signal/expiry; [x] M4.3 Deterministic replay — 35 tes
- M5 — Risk/exit — **DONE; gate LULUS**
  - [x] M5.1 Sizing/exposure; [x] M5.2 Reservation; [x] M5.3 Exit/kill switch — 38 tes
- M6 — Ledger/simulator: **DONE; gate LULUS**
  - [x] M6.1 Intent/attempt — 39 tes; [x] M6.2 State machine — 40 tes; [x] M6.3 Restart/reconciliation — 41 tes
- M7 — Backtest/label: [x] M7.1 Time replay — 42 tes; [ ] M7.2 Cost model; [ ] M7.3 TP/SL/no-route labels
- M8 — Strategy validation: [ ] M8.1 Freeze experiment; [ ] M8.2 Walk-forward/holdout; [ ] M8.3 Stress/report
- M9 — Telegram/paper: [ ] M9.1 Allowlist/commands; [ ] M9.2 Approval TTL; [ ] M9.3 Forward paper
- M10 — Execution integration: [ ] M10.1 Quote/route; [ ] M10.2 Decode/simulation; [ ] M10.3 Signer boundary/status
- M11 — Limited live: [ ] M11.1 Gate/capital/policy; [ ] M11.2 Authorized semi-auto; [ ] M11.3 Actual-fill reconciliation
- M12 — Add-ons: [ ] M12.1 Advanced on-chain; [ ] M12.2 Anomaly ablation; [ ] M12.3 Social/LLM budget/evaluation
- M13 — Full automation: [ ] M13.1 Gate audit; [ ] M13.2 Recovery/runbook; [ ] M13.3 Activation/evaluation

## Aturan update
- Persentase = task Mx.y SELESAI / total task; task aktif/blocked tidak mendapat kredit parsial.
- Regresi → task asal + feature terkait `REOPENED`; perbaiki sebelum fitur baru.
- Bukti rinci tetap di `docs/tasks/Mx.y.md`/`CURRENT.md`, **bukan** di file ini.
- Saat status berubah, update ringkasan + baris task saja. Jangan menambah checkbox pemeriksaan generik atau log tool.
