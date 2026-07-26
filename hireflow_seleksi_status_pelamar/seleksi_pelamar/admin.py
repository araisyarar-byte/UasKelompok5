from django.contrib import admin
from .models import Pelamar, RiwayatStatus

@admin.register(Pelamar)
class PelamarAdmin(admin.ModelAdmin):
    list_display = ('kode_pendaftaran', 'nama_lengkap', 'posisi_dilamar', 'pendidikan_terakhir', 'status_lamaran')
    list_filter = ('status_lamaran', 'pendidikan_terakhir', 'posisi_dilamar')
    search_fields = ('kode_pendaftaran', 'nama_lengkap', 'email', 'jurusan')

@admin.register(RiwayatStatus)
class RiwayatStatusAdmin(admin.ModelAdmin):
    list_display = ('pelamar', 'status_sebelumnya', 'status_baru', 'diubah_oleh', 'diubah_pada')
    readonly_fields = ('pelamar', 'status_sebelumnya', 'status_baru', 'catatan', 'diubah_oleh', 'diubah_pada')
