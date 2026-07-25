from django.contrib import admin
from django.utils.html import format_html

from .models import DokumenPelamar, ProfilPelamar


class DokumenPelamarInline(admin.StackedInline):
    model = DokumenPelamar
    extra = 0
    max_num = 1
    can_delete = False
    fields = ('cv', 'tautan_cv', 'ijazah', 'tautan_ijazah', 'diperbarui_pada')
    readonly_fields = ('tautan_cv', 'tautan_ijazah', 'diperbarui_pada')

    @admin.display(description='Buka CV')
    def tautan_cv(self, obj):
        if obj and obj.cv:
            return format_html('<a href="{}" target="_blank">Lihat / Unduh CV</a>', obj.cv.url)
        return '-'

    @admin.display(description='Buka Ijazah')
    def tautan_ijazah(self, obj):
        if obj and obj.ijazah:
            return format_html('<a href="{}" target="_blank">Lihat / Unduh Ijazah</a>', obj.ijazah.url)
        return '-'


@admin.register(ProfilPelamar)
class ProfilPelamarAdmin(admin.ModelAdmin):
    list_display = (
        'kode_pendaftaran',
        'nama_lengkap',
        'email',
        'nomor_hp',
        'pendidikan_terakhir',
        'status_berkas',
        'dibuat_pada',
    )
    list_filter = ('status_berkas', 'pendidikan_terakhir', 'jenis_kelamin', 'dibuat_pada')
    search_fields = ('kode_pendaftaran', 'user__first_name', 'user__last_name', 'user__email', 'nik', 'nomor_hp')
    list_per_page = 25
    readonly_fields = ('kode_pendaftaran', 'dibuat_pada', 'diperbarui_pada')
    inlines = [DokumenPelamarInline]
    fieldsets = (
        ('Akun Pelamar', {'fields': ('user', 'kode_pendaftaran')}),
        ('Identitas', {'fields': ('nik', 'nomor_hp', 'jenis_kelamin', 'pendidikan_terakhir', 'jurusan', 'alamat')}),
        ('Pemeriksaan Berkas', {'fields': ('status_berkas', 'catatan_admin')}),
        ('Waktu', {'fields': ('dibuat_pada', 'diperbarui_pada')}),
    )

    @admin.display(description='Nama Lengkap', ordering='user__first_name')
    def nama_lengkap(self, obj):
        return obj.user.get_full_name() or obj.user.username

    @admin.display(description='Email', ordering='user__email')
    def email(self, obj):
        return obj.user.email


@admin.register(DokumenPelamar)
class DokumenPelamarAdmin(admin.ModelAdmin):
    list_display = ('profil', 'cv_link', 'ijazah_link', 'diperbarui_pada')
    search_fields = ('profil__kode_pendaftaran', 'profil__user__email', 'profil__nik')
    readonly_fields = ('diperbarui_pada',)

    @admin.display(description='CV')
    def cv_link(self, obj):
        return format_html('<a href="{}" target="_blank">Buka CV</a>', obj.cv.url) if obj.cv else '-'

    @admin.display(description='Ijazah')
    def ijazah_link(self, obj):
        return format_html('<a href="{}" target="_blank">Buka Ijazah</a>', obj.ijazah.url) if obj.ijazah else '-'
