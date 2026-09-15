# Product requirements

Meme AI Trader mengumpulkan dan mengevaluasi peluang token Solana secara bertahap. Target akhir automation, tetapi pengembangan dimulai dari data `collect_only`; tidak ada janji profit atau aktivasi live otomatis.

- Stack: Python, PostgreSQL, Birdeye; Solana RPC, GoPlus, Jupiter, Telegram, dan LLM pada milestone terkait.
- Default: Windows, bahasa dokumentasi Indonesia, identifier kode Inggris, anggaran layanan baru Rp0.
- Safety: LLM tidak mengakses signer; data/safety/risk gate mendahului entry; paper/replay tidak boleh mengirim transaksi live.
- Belum ditetapkan: modal, parameter live, universe, provider plan, limit risiko, dan API access. Tidak boleh diisi dengan asumsi.

Urutan pekerjaan dan gate ada di `ROADMAP.md`; invariants teknis ada di `BLUEPRINT.md`.
