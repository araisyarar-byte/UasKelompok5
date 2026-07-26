from django import forms
from .models import Pelamar


class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Pelamar
        fields = ['status_lamaran', 'catatan_admin']
        widgets = {
            'status_lamaran': forms.Select(attrs={'class': 'form-control'}),
            'catatan_admin': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 5,
                'placeholder': 'Tuliskan hasil review, kekurangan, atau tindak lanjut...',
            }),
        }

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('status_lamaran') == 'ditolak' and not cleaned.get('catatan_admin', '').strip():
            self.add_error('catatan_admin', 'Alasan penolakan wajib diisi.')
        return cleaned
