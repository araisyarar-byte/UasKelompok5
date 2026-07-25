import secrets
from pathlib import Path

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models

MAX_UPLOAD_SIZE = 2 * 1024 * 1024


def validate_file_size(file):
    if file.size > MAX_UPLOAD_SIZE:
        raise ValidationError('Ukuran file maksimal 2 MB.')


def generate_registration_code():
    return f'HF-{secrets.token_hex(4).upper()}'


def upload_cv(instance, filename):
    suffix = Path(filename).suffix.lower()
    return f'pelamar/{instance.profil.kode_pendaftaran}/cv{suffix}'


def upload_ijazah(instance, filename):
    suffix = Path(filename).suffix.lower()
    return f'pelamar/{instance.profil.kode_pendaftaran}/ijazah{suffix}'


class ProfilPelamar(models.Model):
    JENIS_KELAMIN = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]

    PENDIDIKAN = [
        ('SMA/SMK', 'SMA/SMK'),
        ('D3', 'D3'),
        ('D4', 'D4'),
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
    ]

    STATUS = [
        ('baru', 'Baru'),
        ('verifikasi', 'Verifikasi Berkas'),
        ('lengkap', 'Berkas Lengkap'),
        ('tidak_lengkap', 'Berkas Tidak Lengkap'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profil_pelamar',
        verbose_name='Akun pengguna',
    )
    kode_pendaftaran = models.CharField(
        max_length=20,
        unique=True,
        default=generate_registration_code,
        editable=False,
    )
    nik = models.CharField(
        max_length=16,
        unique=True,
        validators=[RegexValidator(r'^\d{16}$', 'NIK harus terdiri dari 16 digit angka.')],
    )
    nomor_hp = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^(?:\+62|62|0)[0-9]{9,13}$', 'Format nomor HP tidak valid.')],
    )
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN)
    pendidikan_terakhir = models.CharField(max_length=10, choices=PENDIDIKAN)
    jurusan = models.CharField(max_length=120)
    alamat = models.TextField()
    status_berkas = models.CharField(max_length=20, choices=STATUS, default='baru')
    catatan_admin = models.TextField(blank=True)
    dibuat_pada = models.DateTimeField(auto_now_add=True)
    diperbarui_pada = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-dibuat_pada']
        verbose_name = 'Profil Pelamar'
        verbose_name_plural = 'Profil Pelamar'

    def __str__(self):
        return f'{self.user.get_full_name() or self.user.username} ({self.kode_pendaftaran})'


class DokumenPelamar(models.Model):
    profil = models.OneToOneField(
        ProfilPelamar,
        on_delete=models.CASCADE,
        related_name='dokumen',
    )
    cv = models.FileField(
        upload_to=upload_cv,
        validators=[
            FileExtensionValidator(['pdf', 'doc', 'docx']),
            validate_file_size,
        ],
        help_text='PDF, DOC, atau DOCX. Maksimal 2 MB.',
    )
    ijazah = models.FileField(
        upload_to=upload_ijazah,
        validators=[
            FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png']),
            validate_file_size,
        ],
        help_text='PDF, JPG, JPEG, atau PNG. Maksimal 2 MB.',
    )
    diperbarui_pada = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Dokumen Pelamar'
        verbose_name_plural = 'Dokumen Pelamar'

    def __str__(self):
        return f'Dokumen {self.profil.kode_pendaftaran}'
