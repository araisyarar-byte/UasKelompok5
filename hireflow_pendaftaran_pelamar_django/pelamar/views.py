from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import PendaftaranPelamarForm


def daftar(request):
    if request.method == 'POST':
        form = PendaftaranPelamarForm(request.POST, request.FILES)
        if form.is_valid():
            profil = form.save()
            request.session['kode_pendaftaran'] = profil.kode_pendaftaran
            messages.success(request, 'Pendaftaran berhasil disimpan.')
            return redirect('pelamar:berhasil')
    else:
        form = PendaftaranPelamarForm()

    return render(request, 'pelamar/daftar.html', {'form': form})


def berhasil(request):
    kode = request.session.pop('kode_pendaftaran', None)
    if not kode:
        return redirect('pelamar:daftar')
    return render(request, 'pelamar/berhasil.html', {'kode_pendaftaran': kode})
