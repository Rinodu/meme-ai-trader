# M1.2 — Kerangka aplikasi dan konfigurasi collect-only

Status: SELESAI pada 2026-09-15. Prasyarat: M1.1 selesai pada commit `84c944b`.

## Tujuan dan lingkup

Buat kerangka Python terkecil yang dapat dijalankan pada Windows dan konfigurasi environment untuk mode aman. Lingkup hanya startup/config; tidak ada database, provider, signer, atau jalur transaksi.

## Acceptance criteria

- Project mendukung Python >=3.11 tanpa dependency runtime eksternal.
- Startup tanpa environment tambahan memakai mode `collect_only`.
- Mode selain `collect_only` ditolak dengan error yang jelas.
- Flag fitur menerima boolean eksplisit; nilai invalid ditolak.
- Credential Birdeye hanya wajib ketika fitur Birdeye aktif.
- Representasi konfigurasi tidak membocorkan API key.
- `.env.example` tidak memuat rahasia dan `.gitignore` melindungi `.env`, virtual environment, serta cache Python.
- Tes konfigurasi terarah lulus pada Python lokal.
- Dokumentasi dan checklist diperbarui; commit/push branch tugas dilakukan bila tersedia.

## Pemeriksaan

Jalankan `py -m unittest discover -s tests -v`, startup default, dan startup dengan mode invalid. Periksa diff serta status Git sebelum commit.

## Bukti

- Implementasi: `meme_ai_trader/config.py`, `meme_ai_trader/__main__.py`, `pyproject.toml`, `.env.example`, dan `.gitignore`.
- `py -m unittest discover -s tests -v`: 5 tes lulus pada Python 3.12.10.
- `py -V:Astral/CPython3.11.16 -m unittest discover -s tests -v`: 5 tes lulus pada Python 3.11.16.
- `py -m meme_ai_trader`: sukses dengan `mode=collect_only birdeye_enabled=False`.
- Startup dengan `MEME_AI_MODE=live_auto`: ditolak dengan exit code 2 dan pesan konfigurasi; tidak ada rahasia dicetak.
- Commit/push dilakukan setelah pemeriksaan diff final; SHA aktual dilaporkan pada serah terima tanpa membuat loop commit dokumentasi.

## Serah terima

Kerangka/config aman tersedia tanpa dependency runtime eksternal atau jalur transaksi. M1.3 tetap bertanggung jawab mengaudit config, dokumentasi setup, dan menutup gate M1.
