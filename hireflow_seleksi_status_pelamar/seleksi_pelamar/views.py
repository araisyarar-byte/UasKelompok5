from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UpdateStatusForm
from .models import Pelamar, RiwayatStatus


@staff_member_required(login_url='login')
def daftar_pelamar(request):
    pelamar = Pelamar.objects.all()
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '')
    posisi = request.GET.get('posisi', '')
    if q:
        pelamar = pelamar.filter(
            Q(nama_lengkap__icontains=q) | Q(kode_pendaftaran__icontains=q)
            | Q(email__icontains=q) | Q(jurusan__icontains=q)
        )
    if status:
        pelamar = pelamar.filter(status_lamaran=status)
    if posisi:
        pelamar = pelamar.filter(posisi_dilamar=posisi)
    context = {
        'pelamar_list': pelamar,
        'status_choices': Pelamar.STATUS_CHOICES,
        'posisi_list': Pelamar.objects.values_list('posisi_dilamar', flat=True).distinct().order_by('posisi_dilamar'),
        'q': q, 'status_aktif': status, 'posisi_aktif': posisi,
        'jumlah_total': Pelamar.objects.count(),
        'jumlah_baru': Pelamar.objects.filter(status_lamaran='baru').count(),
        'jumlah_proses': Pelamar.objects.filter(status_lamaran__in=['review', 'lolos_administrasi', 'wawancara']).count(),
        'jumlah_diterima': Pelamar.objects.filter(status_lamaran='diterima').count(),
    }
    return render(request, 'seleksi_pelamar/daftar.html', context)


@staff_member_required(login_url='login')
def detail_pelamar(request, pk):
    pelamar = get_object_or_404(Pelamar, pk=pk)
    if request.method == 'POST':
        status_lama = pelamar.status_lamaran
        form = UpdateStatusForm(request.POST, instance=pelamar)
        if form.is_valid():
            hasil = form.save()
            if status_lama != hasil.status_lamaran:
                RiwayatStatus.objects.create(
                    pelamar=hasil, status_sebelumnya=status_lama,
                    status_baru=hasil.status_lamaran,
                    catatan=hasil.catatan_admin, diubah_oleh=request.user,
                )
            messages.success(request, f'Status {hasil.nama_lengkap} berhasil diperbarui.')
            return redirect('seleksi_pelamar:detail', pk=hasil.pk)
    else:
        form = UpdateStatusForm(instance=pelamar)
    return render(request, 'seleksi_pelamar/detail.html', {'pelamar': pelamar, 'form': form})
