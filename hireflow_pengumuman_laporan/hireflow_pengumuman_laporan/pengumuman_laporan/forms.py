from django import forms


class CekHasilForm(forms.Form):
    kode_pendaftaran = forms.CharField(
        max_length=30,
        label='Kode Pendaftaran',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contoh: HF-2026-001',
            'autocomplete': 'off',
        }),
    )
    email = forms.EmailField(
        label='Email Terdaftar',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'nama@email.com',
            'autocomplete': 'email',
        }),
    )

    def clean_kode_pendaftaran(self):
        return self.cleaned_data['kode_pendaftaran'].strip().upper()

    def clean_email(self):
        return self.cleaned_data['email'].strip().lower()
