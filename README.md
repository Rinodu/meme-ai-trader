# Meme AI Trader

Bot riset/trading Solana bertahap. Status saat ini: `collect_only`; M2.3 adapter Birdeye read-only telah selesai, tanpa collector aktif atau transaksi.

## Lokal

```powershell
uv sync
uv run python -m unittest discover -s tests
```

Tes integrasi PostgreSQL memerlukan database lokal dan `PGPASSWORD` pada environment proses. Jangan commit credential. Konfigurasi dan batas kerja: `AGENTS.md`; status: `PROGRESS.md`; tugas aktif: `docs/tasks/CURRENT.md`.
