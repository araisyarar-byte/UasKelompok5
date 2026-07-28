from django.contrib import admin
from .models import HasilSeleksi


@admin.action(description='Publikasikan hasil yang dipilih')
def publikasikan(modeladmin, request, queryset):
    for item in queryset:
        item.dipublikasikan = True
        item.save(update_fields=['dipublikasikan', 'tanggal_publikasi', 'diperbarui_pada'])


@admin.action(description='Tarik pengumuman yang dipilih')
def tarik_publikasi(modeladmin, request, queryset):
    for item in queryset:
        item.dipublikasikan = False
        item.save(update_fields=['dipublikasikan', 'tanggal_publikasi', 'diperbarui_pada'])


@admin.register(HasilSeleksi)
class HasilSeleksiAdmin(admin.ModelAdmin):
    list_display = (
        'kode_pendaftaran', 'nama_pelamar', 'posisi_dilamar',
        'status_hasil', 'nilai_akhir', 'dipublikasikan', 'tanggal_publikasi',
    )
    list_filter = ('status_hasil', 'dipublikasikan', 'posisi_dilamar', 'tanggal_melamar')
    search_fields = ('kode_pendaftaran', 'nama_pelamar', 'email', 'posisi_dilamar')
    readonly_fields = ('tanggal_publikasi', 'dibuat_pada', 'diperbarui_pada')
    actions = [publikasikan, tarik_publikasi]
    fieldsets = (
        ('Data Pelamar', {
            'fields': ('kode_pendaftaran', 'nama_pelamar', 'email', 'posisi_dilamar', 'tanggal_melamar')
        }),
        ('Hasil Seleksi', {
            'fields': ('status_hasil', 'nilai_akhir', 'judul_pengumuman', 'isi_pengumuman', 'tindak_lanjut')
        }),
        ('Publikasi', {
            'fields': ('dipublikasikan', 'tanggal_publikasi', 'dibuat_pada', 'diperbarui_pada')
        }),
    )
