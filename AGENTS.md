# AGENTS — Meme AI Trader

## Aturan inti
- Kerjakan **satu subtugas** per siklus sampai implementasi, tes relevan, dokumentasi, commit, dan push branch tugas selesai/terhambat. Jangan lanjut otomatis.
- Target host Windows; gunakan PowerShell untuk panduan pengguna. Jangan mengasumsikan WSL/Docker.
- Pertahankan perilaku lama. Perubahan/penghapusan perilaku memerlukan keputusan pengguna; refactor internal boleh hanya bila perlu untuk tugas.
- Jangan reset/stash/force-push/menimpa pekerjaan pengguna, upgrade dependency, formatting massal, atau merapikan modul lain tanpa kebutuhan.

## Tool dan token
- Coding: Ponytail `full` + YAGNI; pilih solusi terkecil yang benar, reuse kode/native/dependency yang ada.
- Serena: gunakan untuk eksplorasi simbol, referensi, atau refactor lintas file; **jangan** untuk edit trivial pada file yang sudah diketahui.
- RTK: gunakan untuk command terminal yang verbose. Token Saviour boleh mengorkestrasi bila tersedia. Jangan menduplikasi pekerjaan antar-tool.
- Jika tool khusus tidak tersedia, pakai `rg`, output terbatas, dan patch terarah.
- Satu agen default. Batasi tool call, log, diff, dan pembacaan ulang. Batch edit terkait sebelum tes.

## Konteks minimum
Mulai dengan:
1. `AGENTS.md`
2. `AI_CONTEXT.md`
3. `docs/tasks/CURRENT.md`

Lalu baca **hanya bagian relevan** dari `ROADMAP.md`, `FEATURES.md`, kode, dan tes. Baca `PRD.md` bila scope berubah; `BLUEPRINT.md` hanya bagian teknis yang diperlukan. Jangan membaca seluruh repo/dokumentasi/riwayat chat secara default.

Kode + hasil runtime adalah keadaan aktual; dokumen desain adalah target. Jika berbeda, laporkan dan sinkronkan status berdasarkan bukti.

## Verifikasi dan safety
- Mulai dari tes paling sempit yang relevan; perluas regresi bila dampak menyebar. Ikuti `TESTING.md`.
- Jangan melemahkan assertion/menghapus tes untuk membuat hasil lulus.
- Default sistem `collect_only`. Replay/paper tidak boleh mempunyai jalur submit live. Aktivasi live dan merge ke `main` memerlukan instruksi eksplisit.
- Private/API key tidak boleh masuk chat, log, source, atau Git.

## Git dan dokumentasi
- Sebelum edit: cek working tree, branch, remote, dan perubahan pengguna.
- Commit perubahan yang terverifikasi lalu push ke **branch tugas** bila remote tersedia; jangan force-push/main.
- Perbarui: `CURRENT.md` + `AI_CONTEXT.md` setiap handoff; `PROGRESS.md` saat status tugas berubah; `FEATURES.md` bila kontrak/status fitur berubah; `ROADMAP.md` hanya bila urutan/scope berubah; `CHANGELOG.md` untuk perubahan selesai.
- Arsipkan `CURRENT.md` menjadi `docs/tasks/Mx.y.md` ketika berpindah tugas. Hindari duplikasi uraian.

## Definition of done & laporan
`SELESAI` hanya jika acceptance criteria dan pemeriksaan wajib punya bukti. Regresi membuka kembali tugas/fitur terkait dan diprioritaskan sebelum fitur baru.

Laporan akhir singkat: `ID/status | perubahan | tes | commit/push | progres | hambatan | langkah berikutnya`. Jangan mengklaim hasil tanpa bukti.
