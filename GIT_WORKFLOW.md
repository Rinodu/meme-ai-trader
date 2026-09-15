# Git workflow

1. Mulai dari `main` terbaru pada branch `task/<id>-<scope>`.
2. Periksa working tree sebelum edit; jangan menimpa perubahan pengguna.
3. Commit hanya perubahan subtugas yang telah diverifikasi, lalu push ke branch tugas.
4. Buat PR ke `main`; merge hanya atas instruksi eksplisit pengguna.
5. Tidak ada reset destruktif, force-push, atau secret dalam commit.

Dokumentasi status diperbarui dalam commit subtugas atau commit dokumentasi terpisah yang jelas.
