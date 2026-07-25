# HireFlow Rekrutmen Django — Versi Tampilan Rapi

Hasil penggabungan dua folder:

1. `aplikasi_rekrutmen` sebagai proyek Django utama.
2. `hireflow-admin` sebagai acuan desain dashboard.

Semua halaman utama sekarang menggunakan tema HireFlow. Tampilan halaman publik telah dirapikan agar proporsional pada layar laptop dan desktop, sedangkan fungsi tambah, edit, hapus, pencarian, filter, login, database SQLite, dan Django Admin tetap berjalan menggunakan Django.

## Fitur

- Dashboard admin tema HireFlow.
- Halaman kelola lowongan.
- Tambah lowongan.
- Edit lowongan.
- Hapus lowongan dengan konfirmasi.
- Pencarian berdasarkan posisi, perusahaan, atau lokasi.
- Filter lowongan aktif dan nonaktif.
- Halaman publik untuk melihat lowongan aktif dengan tata letak yang sudah dirapikan.
- Lima data contoh bawaan agar halaman tidak kosong saat pertama dijalankan.
- Login dan logout admin.
- Database SQLite.
- Django Admin.
- Tampilan responsif untuk komputer dan HP.

## Akun Admin Bawaan

Gunakan akun berikut untuk pengujian lokal:

- Username: `hireflowadmin`
- Password: `HireFlow123!`

Ganti password sebelum aplikasi diunggah ke hosting atau digunakan secara publik.

## Cara Menjalankan di Git Bash Windows

Buka folder proyek ini di File Explorer. Klik kanan area kosong, lalu pilih **Open Git Bash Here**.

### 1. Membuat virtual environment

```bash
python -m venv venv
```

Perintah ini membuat lingkungan Python khusus proyek agar instalasi Django tidak bercampur dengan proyek lain.

### 2. Mengaktifkan virtual environment

```bash
source venv/Scripts/activate
```

Jika berhasil, bagian awal terminal akan menampilkan `(venv)`.

### 3. Menginstal Django

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Perintah ini menginstal Django yang dibutuhkan proyek.

### 4. Memeriksa dan menyiapkan database

```bash
python manage.py migrate
```

Perintah ini memastikan seluruh tabel database Django sudah tersedia.

### 5. Menjalankan server

```bash
python manage.py runserver
```

Buka alamat berikut di browser:

- Halaman publik: `http://127.0.0.1:8000/`
- Login admin: `http://127.0.0.1:8000/login/`
- Dashboard: `http://127.0.0.1:8000/dashboard/`
- Django Admin: `http://127.0.0.1:8000/admin/`

Untuk menghentikan server, tekan `Ctrl + C` di Git Bash.

## Membuat Akun Admin Baru

```bash
python manage.py createsuperuser
```

Masukkan username, email, dan password sesuai petunjuk terminal.

## Struktur Folder Penting

```text
hireflow_rekrutmen_django_rapi/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── rekrutmen/                 # Pengaturan utama proyek Django
├── administrator/             # Dashboard dan CRUD lowongan admin
├── lowongan/                  # Model dan halaman publik lowongan
├── templates/                 # Template utama dan halaman login
└── static/hireflow/           # CSS dan JavaScript desain HireFlow
```

## Catatan

Folder virtual environment lama tidak dimasukkan ke ZIP karena virtual environment Windows berukuran besar dan sering tidak dapat digunakan di komputer lain. Buat ulang `venv` menggunakan langkah di atas.
