# M12.3 — Social evidence dan bounded LLM narrative

Status: SELESAI pada 2026-09-21.

- Evidence sosial hanya fixture/supplied data; tidak ada provider produksi.
- LLM default disabled dengan budget Rp0; hard stop, cache/dedupe, timeout/retry bounded, dan fallback tidak memblokir eligibility sinyal.
- Ablation menjalankan baseline dan baseline+filter pada dataset, waktu, outcome, dan biaya simulator yang sama; metrik memiliki denominator eksplisit dan outcome hilang dicatat.
- Test M12.3: `uv run python -m unittest tests.test_narrative` — 10/10 lulus.
- Suite penuh: 106/106 lulus; merge `f451601`.
- Tes penuh: `uv run python -m unittest discover -s tests -v` — 96/96 lulus.
- Detail kontrak: `docs/tasks/M12.3.md`.

Berikutnya: M13.1 audit gate signal-only.
