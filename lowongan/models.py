from django.db import models


class Lowongan(models.Model):
    TIPE_PEKERJAAN = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('magang', 'Magang'),
        ('freelance', 'Freelance'),
        ('kontrak', 'Kontrak'),
    ]

    judul = models.CharField(
        max_length=150,
        verbose_name='Posisi Pekerjaan'
    )

    perusahaan = models.CharField(
        max_length=150
    )

    lokasi = models.CharField(
        max_length=150
    )

    tipe_pekerjaan = models.CharField(
        max_length=20,
        choices=TIPE_PEKERJAAN
    )

    deskripsi = models.TextField()

    kualifikasi = models.TextField(
        blank=True
    )

    batas_lamaran = models.DateField(
        blank=True,
        null=True
    )

    status_aktif = models.BooleanField(
        default=True
    )

    dibuat_pada = models.DateTimeField(
        auto_now_add=True
    )

    diperbarui_pada = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-dibuat_pada']
        verbose_name = 'Lowongan'
        verbose_name_plural = 'Lowongan'

    def __str__(self):
        return f'{self.judul} - {self.perusahaan}'
# Create your models here.
