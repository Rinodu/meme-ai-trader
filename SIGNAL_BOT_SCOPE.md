# Scope produk — Signal Bot

Status: **ACCEPTED** pada 16 September 2026. Dokumen ini menggantikan bagian blueprint/roadmap yang menyatakan bot akan melakukan eksekusi transaksi otomatis.

## Perilaku produk

Bot memindai pasar Solana, memilih **nol atau satu kandidat terbaik** pada setiap siklus evaluasi, lalu mengirim sinyal ke Telegram pribadi Edhu. Tidak ada sinyal jika tidak ada kandidat yang melampaui threshold strategi dan quality gate.

Setiap sinyal memuat mint address, nama/simbol bila tersedia, alasan yang dapat diaudit, entry zone, invalidation/stop, target, rencana exit, maksimum waktu hold, serta waktu kedaluwarsa sinyal. Bot memantau sinyal dan mengirim pembaruan `STILL_VALID`, `TAKE_PROFIT`, `EXIT`, `INVALIDATED`, atau `TIME_EXPIRED`, disertai alasan. Edhu melakukan buy/sell secara manual.

## Peluang dan waktu hold

Bot tidak boleh menyebut angka “peluang pump” hanya karena score/LLM confidence. Jika model belum terkalibrasi dan diuji out-of-sample, tampilkan `signal_score` dan `evidence_quality`, dengan teks “bukan probabilitas.”

Setelah label dan evaluasi memadai, bot boleh menampilkan `P(TP sebelum SL dalam horizon H)` berikut versi model, periode evaluasi, ukuran sampel, dan status kalibrasi. Angka itu adalah estimasi historis bersyarat, bukan janji hasil. “Hold berapa lama” adalah maksimal horizon; exit lebih cepat bila invalidation/exit condition terpenuhi.

## Batas keras

- Tidak ada private key, signer, wallet execution, Jupiter `/execute`, atau transaksi on-chain.
- Tidak ada approval buy/sell Telegram. Perintah Telegram hanya mengatur monitoring, status, dan acknowledgement sinyal.
- Jupiter/quote adapter boleh dipertahankan untuk simulasi kapasitas/biaya dan evaluasi realistis; ia tidak boleh membangun, menandatangani, atau mengirim transaksi.
- Semua mode runtime adalah `collect_only`, `replay`, atau `paper_signal`; tidak ada mode semi-auto/live-auto.
- Signal bot tidak menjamin profit, win rate, atau pump.

## Provider

Telegram pribadi saja. Provider data/security mengikuti keputusan teknis yang sudah ada, dengan Birdeye, Solana RPC, dan GoPlus sebagai kandidat. Jupiter menjadi opsional untuk simulator. Provider/paket spesifik, modal, batas risiko, dan biaya belum disetujui; dokumentasikan sebagai `UNKNOWN` sampai Edhu menetapkannya.

## Acceptance criteria tambahan

- Sinyal terbaik dapat ditelusuri kembali ke kandidat pool dan aturan pemilihannya.
- Tidak ada sinyal ketika data/security/quality wajib tidak valid.
- Pesan Telegram memuat alasan entry dan exit, bukan rekomendasi kosong.
- Update exit berasal dari aturan yang sama dengan backtest/paper.
- Unit/integration test menegaskan tidak ada kode signal-only yang memanggil signing atau submit transaksi.
