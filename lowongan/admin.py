from django.contrib import admin
from .models import Lowongan


@admin.register(Lowongan)
class LowonganAdmin(admin.ModelAdmin):
    list_display = (
        'judul',
        'perusahaan',
        'lokasi',
        'tipe_pekerjaan',
        'status_aktif',
        'batas_lamaran',
    )

    list_filter = (
        'status_aktif',
        'tipe_pekerjaan',
    )

    search_fields = (
        'judul',
        'perusahaan',
        'lokasi',
    )

# Register your models here.
