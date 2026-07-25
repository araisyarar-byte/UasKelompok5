from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from lowongan.models import Lowongan
from .forms import LowonganForm


@login_required
def dashboard(request):
    daftar_lowongan = Lowongan.objects.all()
    context = {
        'jumlah_lowongan': daftar_lowongan.count(),
        'jumlah_aktif': daftar_lowongan.filter(status_aktif=True).count(),
        'jumlah_nonaktif': daftar_lowongan.filter(status_aktif=False).count(),
        'lowongan_terbaru': daftar_lowongan[:5],
    }
    return render(request, 'administrator/dashboard.html', context)


@login_required
def kelola_lowongan(request):
    keyword = request.GET.get('q', '').strip()
    status = request.GET.get('status', 'semua')

    daftar_lowongan = Lowongan.objects.all()

    if keyword:
        daftar_lowongan = daftar_lowongan.filter(
            Q(judul__icontains=keyword)
            | Q(perusahaan__icontains=keyword)
            | Q(lokasi__icontains=keyword)
        )

    if status == 'aktif':
        daftar_lowongan = daftar_lowongan.filter(status_aktif=True)
    elif status == 'nonaktif':
        daftar_lowongan = daftar_lowongan.filter(status_aktif=False)

    semua_lowongan = Lowongan.objects.all()
    context = {
        'daftar_lowongan': daftar_lowongan,
        'jumlah_lowongan': semua_lowongan.count(),
        'jumlah_aktif': semua_lowongan.filter(status_aktif=True).count(),
        'jumlah_nonaktif': semua_lowongan.filter(status_aktif=False).count(),
        'keyword': keyword,
        'status_filter': status,
    }
    return render(request, 'administrator/kelola_lowongan.html', context)


@login_required
def tambah_lowongan(request):
    if request.method == 'POST':
        form = LowonganForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lowongan berhasil ditambahkan.')
            return redirect('administrator:kelola_lowongan')
    else:
        form = LowonganForm()

    return render(
        request,
        'administrator/form_lowongan.html',
        {
            'form': form,
            'judul_halaman': 'Tambah Lowongan',
            'subjudul_halaman': 'Lengkapi informasi pekerjaan yang akan dipublikasikan.',
            'teks_tombol': 'Simpan Lowongan',
        },
    )


@login_required
def edit_lowongan(request, pk):
    lowongan = get_object_or_404(Lowongan, pk=pk)

    if request.method == 'POST':
        form = LowonganForm(request.POST, instance=lowongan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lowongan berhasil diperbarui.')
            return redirect('administrator:kelola_lowongan')
    else:
        form = LowonganForm(instance=lowongan)

    return render(
        request,
        'administrator/form_lowongan.html',
        {
            'form': form,
            'judul_halaman': 'Edit Lowongan',
            'subjudul_halaman': f'Perbarui informasi lowongan {lowongan.judul}.',
            'teks_tombol': 'Simpan Perubahan',
        },
    )


@login_required
def hapus_lowongan(request, pk):
    lowongan = get_object_or_404(Lowongan, pk=pk)

    if request.method == 'POST':
        lowongan.delete()
        messages.success(request, 'Lowongan berhasil dihapus.')
        return redirect('administrator:kelola_lowongan')

    return render(
        request,
        'administrator/hapus_lowongan.html',
        {'lowongan': lowongan},
    )
