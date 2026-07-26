from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from seleksi_pelamar.models import Pelamar

class Command(BaseCommand):
    help = 'Membuat akun admin dan data pelamar contoh.'

    def handle(self, *args, **options):
        admin, created = User.objects.get_or_create(username='admin', defaults={'is_staff': True, 'is_superuser': True})
        if created:
            admin.set_password('admin123')
            admin.save()
        contoh = [
            ('HF-2026-001', 'Alya Putri', 'alya@example.com', '081234567801', 'UI/UX Designer', 'S1', 'Desain Komunikasi Visual', 2, 'Figma, User Research, Prototyping'),
            ('HF-2026-002', 'Raka Pratama', 'raka@example.com', '081234567802', 'Backend Developer', 'S1', 'Informatika', 1, 'Python, Django, MySQL, REST API'),
            ('HF-2026-003', 'Nadia Aulia', 'nadia@example.com', '081234567803', 'HR Staff', 'S1', 'Psikologi', 3, 'Recruitment, Interview, Microsoft Office'),
            ('HF-2026-004', 'Dimas Saputra', 'dimas@example.com', '081234567804', 'Backend Developer', 'D3', 'Teknik Informatika', 2, 'PHP, MySQL, Git'),
        ]
        for data in contoh:
            Pelamar.objects.get_or_create(kode_pendaftaran=data[0], defaults={
                'nama_lengkap': data[1], 'email': data[2], 'nomor_hp': data[3],
                'posisi_dilamar': data[4], 'pendidikan_terakhir': data[5],
                'jurusan': data[6], 'pengalaman_tahun': data[7], 'keahlian': data[8],
            })
        self.stdout.write(self.style.SUCCESS('Data demo siap. Login: admin / admin123'))
