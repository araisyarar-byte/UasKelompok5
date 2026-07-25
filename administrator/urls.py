from django.urls import path
from . import views

app_name = 'administrator'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lowongan/', views.kelola_lowongan, name='kelola_lowongan'),
    path('lowongan/tambah/', views.tambah_lowongan, name='tambah_lowongan'),
    path('lowongan/edit/<int:pk>/', views.edit_lowongan, name='edit_lowongan'),
    path('lowongan/hapus/<int:pk>/', views.hapus_lowongan, name='hapus_lowongan'),
]
