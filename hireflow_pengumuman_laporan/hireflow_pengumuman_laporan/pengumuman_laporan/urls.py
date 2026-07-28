from django.urls import path
from . import views

app_name = 'pengumuman_laporan'

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('hasil/', views.cek_hasil, name='cek_hasil'),
    path('laporan/', views.laporan, name='laporan'),
    path('laporan/cetak/', views.cetak_laporan, name='cetak_laporan'),
    path('laporan/ekspor-csv/', views.ekspor_csv, name='ekspor_csv'),
]
