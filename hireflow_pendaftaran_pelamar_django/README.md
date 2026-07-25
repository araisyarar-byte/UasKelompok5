# HireFlow — Pendaftaran Pelamar & Unggah Berkas (Django)

Project ini merupakan **bagian mandiri/terpisah** untuk tugas:

> Pendaftaran Pelamar & Unggah Berkas — membuat form registrasi akun pelamar serta fitur upload dokumen seperti CV dan ijazah.

Project ini tidak digabungkan ke ZIP HireFlow utama. Desainnya mengikuti gaya visual HireFlow yang diberikan sebagai referensi.

## Fitur

- Registrasi akun pelamar menggunakan Django User.
- Nama lengkap, email, nomor HP, dan kata sandi.
- NIK, jenis kelamin, pendidikan terakhir, jurusan, dan alamat.
- Upload CV: PDF, DOC, atau DOCX, maksimal 2 MB.
- Upload ijazah: PDF, JPG, JPEG, atau PNG, maksimal 2 MB.
- Validasi email dan NIK agar tidak ganda.
- Password disimpan menggunakan sistem hashing Django.
- Nomor pendaftaran otomatis.
- Penyimpanan dokumen pada folder `media/pelamar/`.
- Django Administration untuk melihat profil, mengunduh CV/ijazah, dan mengubah status berkas.
- Database SQLite terpisah.
- Tampilan responsif mengikuti tema HireFlow.

## Struktur Project

```text
hireflow_pendaftaran_pelamar_django/
├── manage.py
├── requirements.txt
├── rekrutmen/
├── pelamar/
├── templates/
├── static/
├── media/
├── jalankan_windows.bat
└── jalankan_git_bash.sh
```

## Cara Menjalankan di Windows / Git Bash

Masuk ke folder project:

```bash
cd ~/Downloads/hireflow_pendaftaran_pelamar_django
```

Buat virtual environment:

```bash
python -m venv venv
```

Aktifkan melalui Git Bash:

```bash
source venv/Scripts/activate
```

Instal kebutuhan:

```bash
pip install -r requirements.txt
```

Buat tabel database:

```bash
python manage.py migrate
```

Buat akun administrator:

```bash
python manage.py createsuperuser
```

Jalankan server:

```bash
python manage.py runserver
```

Buka form pelamar:

```text
http://127.0.0.1:8000/
```

Buka Django Administration:

```text
http://127.0.0.1:8000/admin/
```

## Cara Cepat

Klik dua kali `jalankan_windows.bat`, atau di Git Bash jalankan:

```bash
bash jalankan_git_bash.sh
```

Pada pertama kali menjalankan, buat superuser secara manual menggunakan:

```bash
python manage.py createsuperuser
```
