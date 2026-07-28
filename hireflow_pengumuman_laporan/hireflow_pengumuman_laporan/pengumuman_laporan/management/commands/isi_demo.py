from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from pengumuman_laporan.models import HasilSeleksi


class Command(BaseCommand):
    help = 'Membuat akun admin dan data pengumuman contoh.'

    def handle(self, *args, **options):
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'is_staff': True,
                'is_superuser': True,
                'email': 'admin@hireflow.local',
            },
        )
        if created:
            admin.set_password('admin123')
            admin.save()
        else:
            changed = False
            if not admin.is_staff:
                admin.is_staff = True
                changed = True
            if not admin.is_superuser:
                admin.is_superuser = True
                changed = True
            if changed:
                admin.save(update_fields=['is_staff', 'is_superuser'])

        hari_ini = date.today()
        contoh = [
            {
                'kode_pendaftaran': 'HF-2026-001', 'nama_pelamar': 'Alya Putri',
                'email': 'alya@example.com', 'posisi_dilamar': 'UI/UX Designer',
                'tanggal_melamar': hari_ini - timedelta(days=24), 'status_hasil': 'diterima',
                'nilai_akhir': Decimal('88.50'), 'dipublikasikan': True,
                'judul_pengumuman': 'Selamat, Anda Diterima!',
                'isi_pengumuman': 'Berdasarkan seluruh rangkaian seleksi, Anda dinyatakan diterima sebagai UI/UX Designer di HireFlow.',
                'tindak_lanjut': 'Silakan mengonfirmasi kesediaan paling lambat 30 Juli 2026 melalui email HR.',
            },
            {
                'kode_pendaftaran': 'HF-2026-002', 'nama_pelamar': 'Raka Pratama',
                'email': 'raka@example.com', 'posisi_dilamar': 'Backend Developer',
                'tanggal_melamar': hari_ini - timedelta(days=22), 'status_hasil': 'wawancara',
                'nilai_akhir': Decimal('81.25'), 'dipublikasikan': True,
                'judul_pengumuman': 'Undangan Tahap Wawancara',
                'isi_pengumuman': 'Anda lolos ke tahap wawancara untuk posisi Backend Developer.',
                'tindak_lanjut': 'Wawancara dilaksanakan 29 Juli 2026 pukul 10.00 WIB melalui Google Meet.',
            },
            {
                'kode_pendaftaran': 'HF-2026-003', 'nama_pelamar': 'Nadia Aulia',
                'email': 'nadia@example.com', 'posisi_dilamar': 'HR Staff',
                'tanggal_melamar': hari_ini - timedelta(days=20), 'status_hasil': 'ditolak',
                'nilai_akhir': Decimal('70.00'), 'dipublikasikan': True,
                'judul_pengumuman': 'Informasi Hasil Seleksi',
                'isi_pengumuman': 'Terima kasih telah mengikuti proses rekrutmen. Pada periode ini Anda belum dapat melanjutkan ke tahap berikutnya.',
                'tindak_lanjut': 'Data Anda akan disimpan selama enam bulan untuk peluang yang relevan.',
            },
            {
                'kode_pendaftaran': 'HF-2026-004', 'nama_pelamar': 'Dimas Saputra',
                'email': 'dimas@example.com', 'posisi_dilamar': 'Backend Developer',
                'tanggal_melamar': hari_ini - timedelta(days=18), 'status_hasil': 'lolos_administrasi',
                'nilai_akhir': Decimal('78.75'), 'dipublikasikan': True,
                'judul_pengumuman': 'Lolos Seleksi Administrasi',
                'isi_pengumuman': 'Dokumen dan kualifikasi awal Anda memenuhi persyaratan seleksi administrasi.',
                'tindak_lanjut': 'Silakan menunggu informasi jadwal tes teknis melalui email terdaftar.',
            },
            {
                'kode_pendaftaran': 'HF-2026-005', 'nama_pelamar': 'Siti Rahma',
                'email': 'siti@example.com', 'posisi_dilamar': 'Finance Staff',
                'tanggal_melamar': hari_ini - timedelta(days=14), 'status_hasil': 'proses',
                'nilai_akhir': None, 'dipublikasikan': False,
                'judul_pengumuman': 'Hasil Seleksi Sedang Diproses',
                'isi_pengumuman': 'Tim rekrutmen masih melakukan evaluasi terhadap lamaran Anda.',
                'tindak_lanjut': 'Pantau kembali halaman ini secara berkala.',
            },
            {
                'kode_pendaftaran': 'HF-2026-006', 'nama_pelamar': 'Bima Aditya',
                'email': 'bima@example.com', 'posisi_dilamar': 'Digital Marketing',
                'tanggal_melamar': hari_ini - timedelta(days=12), 'status_hasil': 'diterima',
                'nilai_akhir': Decimal('91.00'), 'dipublikasikan': True,
                'judul_pengumuman': 'Selamat Bergabung di HireFlow',
                'isi_pengumuman': 'Anda dinyatakan diterima untuk posisi Digital Marketing.',
                'tindak_lanjut': 'Lengkapi dokumen onboarding melalui email yang telah dikirimkan.',
            },
            {
                'kode_pendaftaran': 'HF-2026-007', 'nama_pelamar': 'Intan Maharani',
                'email': 'intan@example.com', 'posisi_dilamar': 'UI/UX Designer',
                'tanggal_melamar': hari_ini - timedelta(days=9), 'status_hasil': 'ditolak',
                'nilai_akhir': Decimal('72.50'), 'dipublikasikan': True,
                'judul_pengumuman': 'Informasi Hasil Seleksi',
                'isi_pengumuman': 'Kami menghargai waktu dan usaha Anda. Pada proses kali ini, Anda belum dapat melanjutkan.',
                'tindak_lanjut': 'Anda dapat melamar kembali pada lowongan berikutnya.',
            },
            {
                'kode_pendaftaran': 'HF-2026-008', 'nama_pelamar': 'Farhan Rizky',
                'email': 'farhan@example.com', 'posisi_dilamar': 'Backend Developer',
                'tanggal_melamar': hari_ini - timedelta(days=6), 'status_hasil': 'wawancara',
                'nilai_akhir': Decimal('84.25'), 'dipublikasikan': False,
                'judul_pengumuman': 'Undangan Tahap Wawancara',
                'isi_pengumuman': 'Anda lolos ke tahap wawancara untuk posisi Backend Developer.',
                'tindak_lanjut': 'Jadwal akan diumumkan setelah finalisasi pewawancara.',
            },
        ]

        for item in contoh:
            kode = item.pop('kode_pendaftaran')
            HasilSeleksi.objects.update_or_create(kode_pendaftaran=kode, defaults=item)

        self.stdout.write(self.style.SUCCESS(
            'Data demo siap. Login admin: admin / admin123. '
            'Contoh pelamar: HF-2026-001 / alya@example.com'
        ))
