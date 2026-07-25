from django.urls import path

from . import views

app_name = 'pelamar'

urlpatterns = [
    path('', views.daftar, name='daftar'),
    path('berhasil/', views.berhasil, name='berhasil'),
]
