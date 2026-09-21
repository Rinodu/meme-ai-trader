# Changelog

## Paket dokumen 1.0 — 2026-09-15

- Menambahkan aturan kerja sesuai pilihan Edhu, roadmap M1–M13, kontrak fitur, protokol tes/Git, kebijakan token, prompt, dan task awal.
- Menyertakan BLUEPRINT.md v2 sebagai rancangan teknis.
- Semua fitur aplikasi berstatus PLANNED. Belum mengklaim implementasi, backtest, koneksi provider, atau trading berjalan.

Tambahkan entri untuk perubahan selesai: task ID, perilaku berubah, bukti pengujian, serta keterbatasan relevan. Riwayat percobaan gagal tetap berada di catatan task/insiden, tidak disamarkan sebagai rilis selesai.

## Paket dokumen 1.1 — 2026-09-15

- Menambahkan PROGRESS.md dan template form tugas, sesuai delapan pilihan checklist pengguna.
- Menyelaraskan aturan agen, roadmap, fitur, testing, PRD, prompt, dan konteks sesi.
- Persentase awal 0%; semua pekerjaan implementasi tetap belum selesai.
- Struktur, referensi lokal, kesesuaian jumlah subtugas, dan integritas ZIP diperiksa; bukan pengujian aplikasi.

## Paket dokumen 1.2 — 2026-09-16

- Mengubah target produk menjadi Signal Bot Telegram pribadi: kandidat terbaik, entry/exit rationale, maksimal hold, dan update sinyal.
- Menghapus executor, wallet signing, approval buy/sell, semi-auto, serta full-auto dari runtime scope.
- Mempertahankan quote/execution sebagai simulator biaya dan kelayakan exit.
- Menambahkan aturan probability yang terkalibrasi agar score tidak disajikan sebagai peluang pump.

## M12.2 — 2026-09-21

- Menambahkan filter anomaly read-only dan evaluasi ablation baseline vs baseline+filter dengan threshold parameterized.
- Data missing/stale/leakage dipisahkan dari anomaly teramati; selection bias dan status INCONCLUSIVE dicatat.
- Bukti: M12.2 10/10, suite penuh 96/96, merge `fa00785`.

## M12.3 — 2026-09-21

- Menambahkan evidence sosial fixture-only dan narrative enrichment bounded.
- LLM default nonaktif/Rp0, biaya tidak pasti fail-closed, dan fallback tidak mengubah sinyal deterministik.
- Bukti: M12.3 10/10, suite penuh 106/106, merge `f451601`.
