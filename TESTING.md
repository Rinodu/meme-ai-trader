# Testing

Mulai dari tes modul yang berubah, lalu perluas bila kontrak/database/shared infrastructure berubah. Jangan melemahkan assertion atau menjadikan mock sebagai bukti integrasi.

- Config: mode aman, validasi env, secret tidak tampil.
- Data: migrasi, constraint, dedup, UTC, zero vs missing, late event, provider payload.
- Provider: fixture success/error/rate-limit; provider read-only bukan bukti trading live.
- Risk/execution: uji batas, idempotensi, restart, dan reconciliation pada milestone terkait.

Catat perintah dan hasil ringkas di `docs/tasks/CURRENT.md`; SKIPPED/BLOCKED bukan PASS.
