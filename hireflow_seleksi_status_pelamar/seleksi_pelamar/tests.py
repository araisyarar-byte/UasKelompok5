from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Pelamar, RiwayatStatus

class SeleksiPelamarTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user('admin', password='rahasia', is_staff=True)
        self.pelamar = Pelamar.objects.create(
            kode_pendaftaran='HF-TEST-01', nama_lengkap='Pelamar Uji',
            email='uji@example.com', nomor_hp='081234567890',
            posisi_dilamar='Developer', pendidikan_terakhir='S1',
            jurusan='Informatika', pengalaman_tahun=1, keahlian='Python',
        )
        self.client.login(username='admin', password='rahasia')

    def test_daftar_hanya_untuk_admin(self):
        self.assertEqual(self.client.get(reverse('seleksi_pelamar:daftar')).status_code, 200)

    def test_update_status_membuat_riwayat(self):
        response = self.client.post(reverse('seleksi_pelamar:detail', args=[self.pelamar.pk]), {
            'status_lamaran': 'review', 'catatan_admin': 'Kualifikasi sedang diperiksa.',
        })
        self.assertEqual(response.status_code, 302)
        self.pelamar.refresh_from_db()
        self.assertEqual(self.pelamar.status_lamaran, 'review')
        self.assertEqual(RiwayatStatus.objects.filter(pelamar=self.pelamar).count(), 1)

    def test_penolakan_wajib_memiliki_catatan(self):
        response = self.client.post(reverse('seleksi_pelamar:detail', args=[self.pelamar.pk]), {
            'status_lamaran': 'ditolak', 'catatan_admin': '',
        })
        self.assertContains(response, 'Alasan penolakan wajib diisi.')
