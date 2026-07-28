# HireFlow — Pengumuman & Laporan

Proyek Django mandiri untuk bagian **Pengumuman & Laporan**, yaitu menampilkan hasil seleksi kepada pelamar dan membuat rekapitulasi data akhir rekrutmen untuk admin. Proyek ini dibuat terpisah dan tidak digabung dengan ZIP Seleksi & Status Pelamar.

## Fitur Pelamar

- Halaman pengumuman hasil seleksi.
- Verifikasi menggunakan kode pendaftaran dan email terdaftar.
- Hasil tidak ditampilkan sebelum dipublikasikan admin.
- Informasi status, posisi, tanggal pengumuman, pesan, dan tindak lanjut.
- Tampilan responsif untuk laptop dan HP.

## Fitur Admin

- Login staf/admin.
- Ringkasan total pelamar, diterima, belum lolos, dan masih diproses.
- Distribusi status dan rekap per posisi.
- Filter berdasarkan pencarian, status, posisi, publikasi, serta tanggal.
- Cetak laporan atau simpan sebagai PDF melalui browser.
- Ekspor data CSV yang kompatibel dengan Microsoft Excel.
- Pengelolaan pengumuman melalui Django Admin.
- Aksi massal untuk mempublikasikan atau menarik pengumuman.

## Cara Menjalankan di Windows dengan Git Bash

1. Ekstrak ZIP.
2. Masuk ke folder `hireflow_pengumuman_laporan`.
3. Klik kanan di dalam folder, lalu pilih **Open Git Bash Here**.
4. Jalankan:

```bash
bash jalankan_git_bash.sh
```

Atau klik dua kali `jalankan_windows.bat`.

Buka alamat berikut:

- Halaman pelamar: `http://127.0.0.1:8000/`
- Cek hasil: `http://127.0.0.1:8000/hasil/`
- Laporan admin: `http://127.0.0.1:8000/laporan/`
- Django Admin: `http://127.0.0.1:8000/admin/`

## Akun Demo

```text
username: admin
password: admin123
```

Contoh cek hasil pelamar:

```text
Kode Pendaftaran: HF-2026-001
Email: alya@example.com
```

## Perintah Manual

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py isi_demo
python manage.py runserver
```

## Struktur Bagian Utama

```text
pengumuman_laporan/
├── models.py
├── views.py
├── forms.py
├── urls.py
├── admin.py
├── tests.py
├── management/commands/isi_demo.py
└── templates/pengumuman_laporan/
```

## Catatan Jika Nanti Digabung dengan Proyek Kelompok

Bagian aplikasi utamanya adalah folder `pengumuman_laporan`. Saat penggabungan, model perlu disesuaikan agar memakai model pelamar milik proyek kelompok, bukan membuat data ganda. Untuk penilaian bagian individu, ZIP ini dapat dijalankan secara mandiri.
