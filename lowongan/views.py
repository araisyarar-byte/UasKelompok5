from django.shortcuts import render
from .models import Lowongan


def daftar_lowongan(request):
    lowongan_aktif = Lowongan.objects.filter(
        status_aktif=True
    )

    return render(
        request,
        'lowongan/daftar_lowongan.html',
        {
            'daftar_lowongan': lowongan_aktif,
        }
    )

# Create your views here.
