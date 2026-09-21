# M12.2 — Anomaly ablation read-only

Status: SELESAI pada 2026-09-21.

- Anomaly filter memakai data `OnChainSnapshot` M12.1 dan aturan parameterized dengan `rule_version`; missing/stale/leakage tetap alasan data, bukan anomaly.
- Ablation menjalankan baseline dan baseline+filter pada dataset, waktu, outcome, dan biaya simulator yang sama; metrik memiliki denominator eksplisit dan outcome hilang dicatat.
- Test M12.2: `uv run python -m unittest tests.test_anomaly_ablation` — 10/10 lulus.
- Tes penuh: `uv run python -m unittest discover -s tests -v` — 96/96 lulus.
- Detail kontrak: `docs/tasks/M12.2.md`.

Berikutnya: M12.3 social/LLM budget dan evaluasi.
