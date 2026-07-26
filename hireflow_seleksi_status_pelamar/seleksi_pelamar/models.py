from django.contrib.auth.models import User
from django.db import models


class Pelamar(models.Model):
    STATUS_CHOICES = [
        ('baru', 'Baru'),
        ('review', 'Sedang Direview'),
        ('lolos_administrasi', 'Lolos Administrasi'),
        ('wawancara', 'Tahap Wawancara'),
        ('diterima', 'Diterima'),
        ('ditolak', 'Ditolak'),
    ]
    PENDIDIKAN_CHOICES = [
        ('SMA/SMK', 'SMA/SMK'), ('D3', 'D3'), ('D4', 'D4'),
        ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'),
    ]

    kode_pendaftaran = models.CharField(max_length=20, unique=True)
    nama_lengkap = models.CharField(max_length=150)
    email = models.EmailField()
    nomor_hp = models.CharField(max_length=20)
    posisi_dilamar = models.CharField(max_length=120)
    pendidikan_terakhir = models.CharField(max_length=10, choices=PENDIDIKAN_CHOICES)
    jurusan = models.CharField(max_length=120)
    pengalaman_tahun = models.PositiveSmallIntegerField(default=0)
    keahlian = models.TextField(help_text='Pisahkan keahlian dengan koma.')
    cv = models.FileField(upload_to='pelamar/cv/', blank=True)
    ijazah = models.FileField(upload_to='pelamar/ijazah/', blank=True)
    status_lamaran = models.CharField(max_length=30, choices=STATUS_CHOICES, default='baru')
    catatan_admin = models.TextField(blank=True)
    dibuat_pada = models.DateTimeField(auto_now_add=True)
    diperbarui_pada = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-dibuat_pada']
        verbose_name_plural = 'Pelamar'

    def __str__(self):
        return f'{self.nama_lengkap} - {self.posisi_dilamar}'


class RiwayatStatus(models.Model):
    pelamar = models.ForeignKey(Pelamar, on_delete=models.CASCADE, related_name='riwayat_status')
    status_sebelumnya = models.CharField(max_length=30, choices=Pelamar.STATUS_CHOICES)
    status_baru = models.CharField(max_length=30, choices=Pelamar.STATUS_CHOICES)
    catatan = models.TextField(blank=True)
    diubah_oleh = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    diubah_pada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-diubah_pada']
        verbose_name_plural = 'Riwayat Status'
