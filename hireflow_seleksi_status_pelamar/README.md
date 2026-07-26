# HireFlow — Seleksi & Perubahan Status Pelamar

Proyek Django mandiri untuk bagian **review kualifikasi oleh admin dan update status lamaran**. ZIP ini sengaja terpisah dari proyek pendaftaran pelamar.

## Fitur

- Login khusus akun staf/admin.
- Ringkasan jumlah pelamar.
- Pencarian berdasarkan nama, kode, email, atau jurusan.
- Filter berdasarkan status dan posisi.
- Halaman detail kualifikasi dan tautan dokumen.
- Perubahan status: Baru, Sedang Direview, Lolos Administrasi, Wawancara, Diterima, atau Ditolak.
- Catatan admin dan validasi alasan penolakan.
- Riwayat perubahan status beserta admin dan waktunya.
- Tampilan responsif.

## Cara menjalankan di Windows

1. Ekstrak ZIP.
2. Buka folder `hireflow_seleksi_status_pelamar` di Git Bash.
3. Jalankan:

```bash
bash jalankan_git_bash.sh
```

Atau klik `jalankan_windows.bat`.

4. Buka `http://127.0.0.1:8000/`
5. Login demo:

```text
username: admin
password: admin123
```

Perintah manual:

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py isi_demo
python manage.py runserver
```

## Catatan penggabungan dengan proyek kelompok

Folder aplikasi utama adalah `seleksi_pelamar`. Jika nanti digabung, pindahkan folder tersebut beserta `static/seleksi_pelamar`, tambahkan `seleksi_pelamar` ke `INSTALLED_APPS`, lalu tambahkan URL aplikasinya. Model dibuat mandiri agar bagian ini dapat dinilai dan dijalankan sendiri.
