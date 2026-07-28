import csv
from datetime import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Avg, Count, Q
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .forms import CekHasilForm
from .models import HasilSeleksi


def beranda(request):
    return render(request, 'pengumuman_laporan/beranda.html')


def cek_hasil(request):
    hasil = None
    sudah_dicari = False
    form = CekHasilForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        sudah_dicari = True
        hasil = HasilSeleksi.objects.filter(
            kode_pendaftaran__iexact=form.cleaned_data['kode_pendaftaran'],
            email__iexact=form.cleaned_data['email'],
            dipublikasikan=True,
        ).first()

    return render(request, 'pengumuman_laporan/cek_hasil.html', {
        'form': form,
        'hasil': hasil,
        'sudah_dicari': sudah_dicari,
    })


def _parse_date(value):
    if not value:
        return None
    try:
        return datetime.strptime(value, '%Y-%m-%d').date()
    except ValueError:
        return None


def _filtered_queryset(request):
    data = HasilSeleksi.objects.all()
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()
    posisi = request.GET.get('posisi', '').strip()
    publikasi = request.GET.get('publikasi', '').strip()
    tanggal_awal_raw = request.GET.get('tanggal_awal', '').strip()
    tanggal_akhir_raw = request.GET.get('tanggal_akhir', '').strip()
    tanggal_awal = _parse_date(tanggal_awal_raw)
    tanggal_akhir = _parse_date(tanggal_akhir_raw)

    if q:
        data = data.filter(
            Q(kode_pendaftaran__icontains=q)
            | Q(nama_pelamar__icontains=q)
            | Q(email__icontains=q)
        )
    if status:
        data = data.filter(status_hasil=status)
    if posisi:
        data = data.filter(posisi_dilamar=posisi)
    if publikasi == 'ya':
        data = data.filter(dipublikasikan=True)
    elif publikasi == 'tidak':
        data = data.filter(dipublikasikan=False)
    if tanggal_awal:
        data = data.filter(tanggal_melamar__gte=tanggal_awal)
    if tanggal_akhir:
        data = data.filter(tanggal_melamar__lte=tanggal_akhir)

    filters = {
        'q': q,
        'status_aktif': status,
        'posisi_aktif': posisi,
        'publikasi_aktif': publikasi,
        'tanggal_awal': tanggal_awal_raw,
        'tanggal_akhir': tanggal_akhir_raw,
    }
    return data, filters


@staff_member_required(login_url='login')
def laporan(request):
    data, filters = _filtered_queryset(request)
    seluruh = HasilSeleksi.objects.all()
    total = seluruh.count()
    diterima = seluruh.filter(status_hasil='diterima').count()
    ditolak = seluruh.filter(status_hasil='ditolak').count()
    dalam_proses = seluruh.filter(status_hasil__in=['proses', 'lolos_administrasi', 'wawancara']).count()
    dipublikasikan = seluruh.filter(dipublikasikan=True).count()
    tingkat_penerimaan = round((diterima / total) * 100, 1) if total else 0

    status_rekap = list(
        seluruh.values('status_hasil')
        .annotate(jumlah=Count('id'))
        .order_by('-jumlah')
    )
    label_status = dict(HasilSeleksi.STATUS_CHOICES)
    for item in status_rekap:
        item['label'] = label_status.get(item['status_hasil'], item['status_hasil'])
        item['persen'] = round((item['jumlah'] / total) * 100, 1) if total else 0

    posisi_rekap = list(
        seluruh.values('posisi_dilamar')
        .annotate(jumlah=Count('id'), rata_nilai=Avg('nilai_akhir'))
        .order_by('-jumlah', 'posisi_dilamar')
    )

    context = {
        **filters,
        'hasil_list': data,
        'status_choices': HasilSeleksi.STATUS_CHOICES,
        'posisi_list': seluruh.values_list('posisi_dilamar', flat=True).distinct().order_by('posisi_dilamar'),
        'jumlah_filter': data.count(),
        'jumlah_total': total,
        'jumlah_diterima': diterima,
        'jumlah_ditolak': ditolak,
        'jumlah_proses': dalam_proses,
        'jumlah_dipublikasikan': dipublikasikan,
        'tingkat_penerimaan': tingkat_penerimaan,
        'status_rekap': status_rekap,
        'posisi_rekap': posisi_rekap,
        'dicetak_pada': timezone.localtime(),
    }
    return render(request, 'pengumuman_laporan/laporan.html', context)


@staff_member_required(login_url='login')
def cetak_laporan(request):
    data, filters = _filtered_queryset(request)
    ringkasan = data.aggregate(
        total=Count('id'),
        diterima=Count('id', filter=Q(status_hasil='diterima')),
        ditolak=Count('id', filter=Q(status_hasil='ditolak')),
        dipublikasikan=Count('id', filter=Q(dipublikasikan=True)),
        rata_nilai=Avg('nilai_akhir'),
    )
    return render(request, 'pengumuman_laporan/cetak_laporan.html', {
        'hasil_list': data,
        'ringkasan': ringkasan,
        'filters': filters,
        'dicetak_pada': timezone.localtime(),
    })


@staff_member_required(login_url='login')
def ekspor_csv(request):
    data, _ = _filtered_queryset(request)
    nama_file = f'laporan-rekrutmen-{timezone.localdate():%Y%m%d}.csv'
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="{nama_file}"'
    response.write('\ufeff')

    writer = csv.writer(response, delimiter=';')
    writer.writerow([
        'No', 'Kode Pendaftaran', 'Nama Pelamar', 'Email', 'Posisi',
        'Tanggal Melamar', 'Status Hasil', 'Nilai Akhir', 'Dipublikasikan',
        'Tanggal Publikasi',
    ])
    for nomor, item in enumerate(data, start=1):
        writer.writerow([
            nomor,
            item.kode_pendaftaran,
            item.nama_pelamar,
            item.email,
            item.posisi_dilamar,
            item.tanggal_melamar.strftime('%d-%m-%Y'),
            item.get_status_hasil_display(),
            item.nilai_akhir if item.nilai_akhir is not None else '',
            'Ya' if item.dipublikasikan else 'Tidak',
            timezone.localtime(item.tanggal_publikasi).strftime('%d-%m-%Y %H:%M') if item.tanggal_publikasi else '',
        ])
    return response
