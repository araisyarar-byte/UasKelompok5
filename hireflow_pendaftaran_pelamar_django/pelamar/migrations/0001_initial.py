# Generated for HireFlow Pendaftaran Pelamar
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.core.validators
import pelamar.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilPelamar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_pendaftaran', models.CharField(default=pelamar.models.generate_registration_code, editable=False, max_length=20, unique=True)),
                ('nik', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(r'^\d{16}$', 'NIK harus terdiri dari 16 digit angka.')])),
                ('nomor_hp', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(r'^(?:\+62|62|0)[0-9]{9,13}$', 'Format nomor HP tidak valid.')])),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=1)),
                ('pendidikan_terakhir', models.CharField(choices=[('SMA/SMK', 'SMA/SMK'), ('D3', 'D3'), ('D4', 'D4'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')], max_length=10)),
                ('jurusan', models.CharField(max_length=120)),
                ('alamat', models.TextField()),
                ('status_berkas', models.CharField(choices=[('baru', 'Baru'), ('verifikasi', 'Verifikasi Berkas'), ('lengkap', 'Berkas Lengkap'), ('tidak_lengkap', 'Berkas Tidak Lengkap')], default='baru', max_length=20)),
                ('catatan_admin', models.TextField(blank=True)),
                ('dibuat_pada', models.DateTimeField(auto_now_add=True)),
                ('diperbarui_pada', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profil_pelamar', to=settings.AUTH_USER_MODEL, verbose_name='Akun pengguna')),
            ],
            options={'verbose_name': 'Profil Pelamar', 'verbose_name_plural': 'Profil Pelamar', 'ordering': ['-dibuat_pada']},
        ),
        migrations.CreateModel(
            name='DokumenPelamar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(help_text='PDF, DOC, atau DOCX. Maksimal 2 MB.', upload_to=pelamar.models.upload_cv, validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx']), pelamar.models.validate_file_size])),
                ('ijazah', models.FileField(help_text='PDF, JPG, JPEG, atau PNG. Maksimal 2 MB.', upload_to=pelamar.models.upload_ijazah, validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png']), pelamar.models.validate_file_size])),
                ('diperbarui_pada', models.DateTimeField(auto_now=True)),
                ('profil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dokumen', to='pelamar.profilpelamar')),
            ],
            options={'verbose_name': 'Dokumen Pelamar', 'verbose_name_plural': 'Dokumen Pelamar'},
        ),
    ]
