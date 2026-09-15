# Blueprint teknis ringkas — Meme AI Trader

Status: rancangan implementasi; **bukan strategi yang terbukti menguntungkan**. Blockchain Solana, baseline short-term momentum. Detail implementasi harus dibuktikan melalui data, tes, dan evaluasi out-of-sample.

## 1. Scope dan invariants
MVP: satu strategi momentum, satu wallet khusus, baseline deterministik lebih dulu. Urutan mode:
`collect_only → backtest → paper → semi_auto → live_auto`.

Invariants:
1. LLM tidak dapat menimpa Risk Engine atau mengakses signer/private key.
2. Entry memerlukan data wajib segar + security gate lulus; `UNKNOWN`/`REJECT` memblokir entry.
3. Exit independen dari gate entry dan tetap tersedia saat entry dipause.
4. Logic strategy/risk/exit sama pada replay/paper/live; adapter execution berbeda.
5. Submit transaksi ≠ fill. Intent, attempt, saldo, fill, dan posisi wajib direkonsiliasi.
6. Parameter live tidak boleh diisi dengan default arbitrer; konfigurasi/gate yang belum lengkap memblokir live.
7. Ledger yang direkonsiliasi dengan on-chain adalah sumber kebenaran posisi.

## 2. Arsitektur
`Collector/raw events → data quality/features → security + strategy → risk → quote/validate/simulate → executor/reconciliation → ledger/position monitor → exit`

Cabang opsional: data tervalidasi → on-chain/anomaly/social/LLM → snapshot fitur → strategy. Analisis kandidat tidak boleh mengalahkan prioritas monitoring, exit, dan reconciliation.

Stack: Python, PostgreSQL; Redis hanya bila dibutuhkan; Birdeye market data; Solana RPC; GoPlus + pemeriksaan on-chain; Jupiter adapter; Telegram; LLM opsional tahap lanjut. Mulai modular monolith/local, VPS bila perlu.

## 3. Data contract
Raw event append-oriented dan fitur turunan dapat dihitung ulang. Minimum:
`event_id, source, source_event_id, schema_version, chain_id, mint_address, pool_address, token_program, decimals, event_time, received_at, source_slot, commitment, price, quote_currency, market_cap, fdv, liquidity, volume windows, buy/sell counts, unique wallets, price-change windows, data_quality_status, missing_fields, raw_payload_reference`.

Aturan:
- Identitas token = chain + mint; symbol/name hanya display.
- UTC; `event_time` dipisah dari `received_at`; backtest hanya boleh memakai data yang sudah tersedia pada waktu keputusan.
- Decimal/integer atomic units untuk uang/jumlah; hindari float untuk saldo.
- Dedup, late/out-of-order events, gap/reconnect/backfill, zero vs missing, serta rejected/dead/no-route candidates harus eksplisit.
- Jangan forward-fill tanpa batas atau menyamakan market cap dengan FDV.

## 4. Discovery & security
Filter murah: valid mint/pool/program → data lengkap/segar → universe usia → liquidity/volume → no duplicate intent/cooldown → security/capacity.

Security status: `PASS | REJECT | UNKNOWN`; hanya PASS boleh lanjut entry. Periksa authority, program/Token-2022 capabilities, liquidity/tradability, dan provider evidence. API gagal/data stale = UNKNOWN, bukan aman. Simpan evidence, waktu/slot, rule version, flags, dan alasan.

## 5. Strategy, risk, quote, exit
Baseline: fitur deterministik seperti momentum, return, volume acceleration, imbalance, liquidity change, volatility/drawdown; jangan menganggap indikator yang berkorelasi sebagai bukti independen.

Strategy contract:
`universe + feature_windows + entry + invalidation + exit + sizing + cooldown + cost_model + version`.
Tetapkan warm-up, timing, missing-data behavior, dan signal expiry.

Risk membedakan notional vs planned loss. Batasi: posisi, portfolio/correlated exposure, daily loss, drawdown, fee reserve, slippage/price impact, quote/data age, dan API cost. Reservasi modal atomik sebelum submit.

Sizing konseptual:
`risk_budget = equity × risk_per_trade_pct`
`risk_notional = risk_budget / estimated_loss_fraction`
`approved = min(risk_notional, position_cap, portfolio_cap, liquidity_cap, spendable_after_fee_reserve)`

Sebelum entry gunakan quote ukuran aktual dan periksa route balik/exit capacity, fee, price impact, min output, serta usia quote. Slippage tolerance adalah batas, bukan biaya aktual.

Exit yang diuji: stop/invalidation, TP, time stop, portfolio reduction, emergency security/liquidity. No route ≠ fill; tandai blocked, alert, retry terbatas, dan valuasi konservatif. Daily-loss pause memblokir entry, bukan risk-reducing exit.

## 6. Transaction lifecycle & control
Pisahkan `intent_id` dari `attempt_id/signature`. State minimal:
`CREATED → READY → SUBMITTED → CONFIRMED → FINALIZED`, dengan `UNKNOWN | FAILED | EXPIRED | CANCELLED` bila relevan.

Network timeout bukan bukti gagal. Jangan membuat replacement sebelum status attempt lama direkonsiliasi. Restart harus merekonsiliasi pending transactions, balances, reservations, dan positions sebelum entry baru.

Sebelum signing: cek intent/approval TTL, reservasi, quote, security, risk; decode dan verifikasi mint/amount/signer/destination/instructions/min-output; simulate; validasi ulang bila payload berubah. Signer terbatas dan tidak menerima instruksi bebas dari LLM.

Control modes:
- `RUNNING`
- `PAUSE_ENTRIES`
- `REDUCE_ONLY`
- `HALT_SIGNING`

Stale feed, loss limit, RPC failure, reconciliation mismatch, repeated failures, atau signer incident memicu mode yang sesuai. Resume hanya setelah penyebab selesai + data segar + reconciliation + otorisasi.

## 7. Telegram & LLM
Telegram memakai allowlist. Approval terikat `intent_id`, token, side, nominal limit, dan expiry; sekali pakai. Setelah approval selalu requote + rerun risk/security. Telegram bukan satu-satunya jalur exit/monitoring.

LLM hanya tahap lanjut/background: output terstruktur, evidence refs, timestamp/expiry, prompt version, timeout/cache/budget. Social text adalah untrusted input. Exit tidak bergantung pada LLM. `score` bukan `probability`; probability hanya dipakai bila target dan kalibrasinya diuji.

## 8. Backtest, paper, dan evaluasi
Replay hanya memakai data point-in-time. Label awal: `TP_FIRST | SL_FIRST | TIMEOUT` plus status seperti `EXIT_UNAVAILABLE/DATA_INSUFFICIENT`; intrabar ambiguity tidak boleh diselesaikan secara optimistis.

Masukkan fee, latency, slippage, impact, unavailable route, reservations, dan failure. Gunakan development → validation → walk-forward/purging → untouched holdout → forward paper. Holdout yang dipakai untuk tuning tidak lagi untouched.

Ukur strategy metrics (net expectancy, PF, drawdown, tail loss, MAE/MFE, exposure/turnover) dan operational metrics (data age, latency, quote→submit, submit→confirm, failures, exit success, duplicates, ledger mismatch, service cost, paper/live deviation). Hasil lemah = `INCONCLUSIVE`, bukan dipaksa PASS.

## 9. Live gate / Definition of Done
Sebelum live: data integrity, security UNKNOWN blocking, risk/reservation/exit, transaction idempotency/reconciliation, illiquid valuation, kill switch/reduce-only, backup/recovery, experiment traceability, costs, stress/holdout/forward evidence, dan paper/live deviation harus punya bukti sesuai acceptance criteria.

Live dan scaling membutuhkan aktivasi eksplisit. Pengembangan/tes tidak memberikan izin penggunaan uang nyata.

## 10. Integrasi
Kontrak provider/API harus diverifikasi saat milestone integrasi karena endpoint/paket/schema dapat berubah. Provider utama: Birdeye, Solana RPC, GoPlus, Jupiter. Simpan tanggal/link verifikasi pada catatan tugas, bukan memperbesar blueprint.

Milestone dan gate operasional ada di `ROADMAP.md`; status aktual di `PROGRESS.md`; kontrak fitur di `FEATURES.md`; tes minimum di `TESTING.md`.
