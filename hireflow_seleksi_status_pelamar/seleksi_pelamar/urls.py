from django.urls import path
from . import views

app_name = 'seleksi_pelamar'
urlpatterns = [
    path('', views.daftar_pelamar, name='daftar'),
    path('pelamar/<int:pk>/', views.detail_pelamar, name='detail'),
]
