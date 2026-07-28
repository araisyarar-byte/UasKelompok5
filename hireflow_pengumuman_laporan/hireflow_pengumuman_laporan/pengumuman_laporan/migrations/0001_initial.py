# Initial migration for HireFlow Pengumuman & Laporan.

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='HasilSeleksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_pendaftaran', models.CharField(max_length=30, unique=True)),
                ('nama_pelamar', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('posisi_dilamar', models.CharField(max_length=120)),
                ('tanggal_melamar', models.DateField(default=django.utils.timezone.localdate)),
                ('status_hasil', models.CharField(choices=[('proses', 'Masih Diproses'), ('lolos_administrasi', 'Lolos Administrasi'), ('wawancara', 'Lolos ke Tahap Wawancara'), ('diterima', 'Diterima'), ('ditolak', 'Belum Lolos')], default='proses', max_length=30)),
                ('nilai_akhir', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('judul_pengumuman', models.CharField(default='Hasil Seleksi Rekrutmen', max_length=180)),
                ('isi_pengumuman', models.TextField(blank=True)),
                ('tindak_lanjut', models.TextField(blank=True, help_text='Contoh: jadwal wawancara atau instruksi pemberkasan.')),
                ('dipublikasikan', models.BooleanField(default=False)),
                ('tanggal_publikasi', models.DateTimeField(blank=True, null=True)),
                ('dibuat_pada', models.DateTimeField(auto_now_add=True)),
                ('diperbarui_pada', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Hasil Seleksi',
                'verbose_name_plural': 'Hasil Seleksi',
                'ordering': ['-tanggal_melamar', 'nama_pelamar'],
                'indexes': [
                    models.Index(fields=['status_hasil'], name='hasil_status_idx'),
                    models.Index(fields=['posisi_dilamar'], name='hasil_posisi_idx'),
                    models.Index(fields=['tanggal_melamar'], name='hasil_tanggal_idx'),
                ],
            },
        ),
    ]
