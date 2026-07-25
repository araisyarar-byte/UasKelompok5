from django.urls import path
from . import views


app_name = 'lowongan'


urlpatterns = [
    path(
        '',
        views.daftar_lowongan,
        name='daftar_lowongan'
    ),
]