from django.db import models
from django.utils import timezone


class HasilSeleksi(models.Model):
    STATUS_CHOICES = [
        ('proses', 'Masih Diproses'),
        ('lolos_administrasi', 'Lolos Administrasi'),
        ('wawancara', 'Lolos ke Tahap Wawancara'),
        ('diterima', 'Diterima'),
        ('ditolak', 'Belum Lolos'),
    ]

    kode_pendaftaran = models.CharField(max_length=30, unique=True)
    nama_pelamar = models.CharField(max_length=150)
    email = models.EmailField()
    posisi_dilamar = models.CharField(max_length=120)
    tanggal_melamar = models.DateField(default=timezone.localdate)
    status_hasil = models.CharField(max_length=30, choices=STATUS_CHOICES, default='proses')
    nilai_akhir = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    judul_pengumuman = models.CharField(max_length=180, default='Hasil Seleksi Rekrutmen')
    isi_pengumuman = models.TextField(blank=True)
    tindak_lanjut = models.TextField(blank=True, help_text='Contoh: jadwal wawancara atau instruksi pemberkasan.')
    dipublikasikan = models.BooleanField(default=False)
    tanggal_publikasi = models.DateTimeField(null=True, blank=True)
    dibuat_pada = models.DateTimeField(auto_now_add=True)
    diperbarui_pada = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-tanggal_melamar', 'nama_pelamar']
        verbose_name = 'Hasil Seleksi'
        verbose_name_plural = 'Hasil Seleksi'
        indexes = [
            models.Index(fields=['status_hasil'], name='hasil_status_idx'),
            models.Index(fields=['posisi_dilamar'], name='hasil_posisi_idx'),
            models.Index(fields=['tanggal_melamar'], name='hasil_tanggal_idx'),
        ]

    def __str__(self):
        return f'{self.kode_pendaftaran} - {self.nama_pelamar}'

    def save(self, *args, **kwargs):
        if self.dipublikasikan and self.tanggal_publikasi is None:
            self.tanggal_publikasi = timezone.now()
        if not self.dipublikasikan:
            self.tanggal_publikasi = None
        super().save(*args, **kwargs)
