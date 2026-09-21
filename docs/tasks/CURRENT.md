# M12.1 — Snapshot on-chain read-only

Status: SELESAI pada 2026-09-21.

- Snapshot memakai schema Solana read-only, validasi Base58 mint, slot, commitment `confirmed`/`finalized`, dan hard safety fields.
- Freshness default 120 detik; status `FRESH`, `STALE`, `PARTIAL`, `MISSING`, atau `INVALID`.
- `allows_signal` false untuk stale/missing/invalid; data yang hilang tetap `null`, bukan nol.
- Test M12.1: `uv run python -m unittest tests.test_onchain_snapshot` — 16/16 lulus.
- Tes penuh: `uv run python -m unittest discover -s tests -v` — 86/86 lulus.
- Detail kontrak: `docs/tasks/M12.1.md`.

Berikutnya: M12.2 anomaly ablation.
