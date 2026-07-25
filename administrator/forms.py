from django import forms
from lowongan.models import Lowongan


class LowonganForm(forms.ModelForm):
    class Meta:
        model = Lowongan

        fields = [
            'judul',
            'perusahaan',
            'lokasi',
            'tipe_pekerjaan',
            'deskripsi',
            'kualifikasi',
            'batas_lamaran',
            'status_aktif',
        ]

        widgets = {
            'judul': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contoh: Web Developer',
                }
            ),

            'perusahaan': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nama perusahaan',
                }
            ),

            'lokasi': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contoh: Jakarta',
                }
            ),

            'tipe_pekerjaan': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'deskripsi': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Tuliskan deskripsi pekerjaan',
                }
            ),

            'kualifikasi': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Tuliskan kualifikasi pelamar',
                }
            ),

            'batas_lamaran': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),

            'status_aktif': forms.CheckboxInput(
                attrs={
                    'class': 'form-check',
                }
            ),
        }