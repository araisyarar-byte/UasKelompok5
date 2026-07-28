from datetime import date
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import HasilSeleksi


class PengumumanLaporanTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user('admin', password='rahasia', is_staff=True)
        self.hasil = HasilSeleksi.objects.create(
            kode_pendaftaran='HF-TEST-001',
            nama_pelamar='Pelamar Uji',
            email='uji@example.com',
            posisi_dilamar='Backend Developer',
            tanggal_melamar=date(2026, 7, 20),
            status_hasil='diterima',
            nilai_akhir=Decimal('90.00'),
            isi_pengumuman='Anda diterima.',
            dipublikasikan=True,
        )

    def test_hasil_publik_bisa_dicek_dengan_identitas_benar(self):
        response = self.client.post(reverse('pengumuman_laporan:cek_hasil'), {
            'kode_pendaftaran': 'hf-test-001',
            'email': 'UJI@example.com',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pelamar Uji')
        self.assertContains(response, 'Anda diterima.')

    def test_hasil_tidak_tampil_bila_email_salah(self):
        response = self.client.post(reverse('pengumuman_laporan:cek_hasil'), {
            'kode_pendaftaran': 'HF-TEST-001',
            'email': 'salah@example.com',
        })
        self.assertContains(response, 'Data pengumuman tidak ditemukan')

    def test_hasil_belum_dipublikasikan_tidak_tampil(self):
        self.hasil.dipublikasikan = False
        self.hasil.save()
        response = self.client.post(reverse('pengumuman_laporan:cek_hasil'), {
            'kode_pendaftaran': 'HF-TEST-001',
            'email': 'uji@example.com',
        })
        self.assertContains(response, 'Data pengumuman tidak ditemukan')

    def test_laporan_hanya_untuk_staf(self):
        response = self.client.get(reverse('pengumuman_laporan:laporan'))
        self.assertEqual(response.status_code, 302)
        self.client.login(username='admin', password='rahasia')
        response = self.client.get(reverse('pengumuman_laporan:laporan'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rekapitulasi Rekrutmen')

    def test_ekspor_csv(self):
        self.client.login(username='admin', password='rahasia')
        response = self.client.get(reverse('pengumuman_laporan:ekspor_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv; charset=utf-8')
        self.assertIn('HF-TEST-001', response.content.decode('utf-8-sig'))
