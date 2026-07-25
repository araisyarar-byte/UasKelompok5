from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction

from .models import DokumenPelamar, ProfilPelamar


class PendaftaranPelamarForm(forms.Form):
    nama_lengkap = forms.CharField(
        max_length=100,
        min_length=3,
        label='Nama Lengkap',
        widget=forms.TextInput(attrs={'placeholder': 'Masukkan nama lengkap', 'autocomplete': 'name'}),
    )
    email = forms.EmailField(
        max_length=150,
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'nama@email.com', 'autocomplete': 'email'}),
    )
    nomor_hp = forms.CharField(
        max_length=20,
        label='Nomor HP',
        widget=forms.TextInput(attrs={'placeholder': '08xxxxxxxxxx', 'inputmode': 'tel'}),
    )
    password1 = forms.CharField(
        label='Kata Sandi',
        widget=forms.PasswordInput(attrs={'placeholder': 'Minimal 8 karakter', 'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label='Konfirmasi Kata Sandi',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ulangi kata sandi', 'autocomplete': 'new-password'}),
    )
    nik = forms.CharField(
        max_length=16,
        min_length=16,
        label='NIK',
        widget=forms.TextInput(attrs={'placeholder': '16 digit NIK', 'inputmode': 'numeric'}),
    )
    jenis_kelamin = forms.ChoiceField(
        choices=[('', 'Pilih jenis kelamin')] + ProfilPelamar.JENIS_KELAMIN,
        label='Jenis Kelamin',
    )
    pendidikan_terakhir = forms.ChoiceField(
        choices=[('', 'Pilih pendidikan')] + ProfilPelamar.PENDIDIKAN,
        label='Pendidikan Terakhir',
    )
    jurusan = forms.CharField(
        max_length=120,
        label='Jurusan',
        widget=forms.TextInput(attrs={'placeholder': 'Contoh: Sistem Informasi'}),
    )
    alamat = forms.CharField(
        min_length=10,
        label='Alamat Lengkap',
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Masukkan alamat tempat tinggal'}),
    )
    cv = forms.FileField(
        label='CV',
        help_text='PDF, DOC, atau DOCX. Maksimal 2 MB.',
    )
    ijazah = forms.FileField(
        label='Ijazah',
        help_text='PDF, JPG, JPEG, atau PNG. Maksimal 2 MB.',
    )
    persetujuan = forms.BooleanField(
        label='Saya menyatakan data dan dokumen yang diberikan benar.',
    )

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(username__iexact=email).exists() or User.objects.filter(email__iexact=email).exists():
            raise ValidationError('Email sudah terdaftar.')
        return email

    def clean_nik(self):
        nik = ''.join(filter(str.isdigit, self.cleaned_data['nik']))
        if len(nik) != 16:
            raise ValidationError('NIK harus terdiri dari 16 digit angka.')
        if ProfilPelamar.objects.filter(nik=nik).exists():
            raise ValidationError('NIK sudah terdaftar.')
        return nik

    def clean_nomor_hp(self):
        nomor = self.cleaned_data['nomor_hp'].replace(' ', '').replace('-', '')
        if not nomor.startswith(('0', '62', '+62')) or not nomor.replace('+', '').isdigit():
            raise ValidationError('Format nomor HP tidak valid.')
        if len(nomor.replace('+', '')) < 10 or len(nomor.replace('+', '')) > 15:
            raise ValidationError('Nomor HP harus berisi 10 sampai 15 digit.')
        return nomor

    def clean_password1(self):
        password = self.cleaned_data['password1']
        validate_password(password)
        return password

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password1') and cleaned.get('password2'):
            if cleaned['password1'] != cleaned['password2']:
                self.add_error('password2', 'Konfirmasi kata sandi tidak sama.')
        return cleaned

    def _validate_document(self, field_name, extensions):
        uploaded = self.cleaned_data.get(field_name)
        if not uploaded:
            return uploaded
        extension = uploaded.name.rsplit('.', 1)[-1].lower() if '.' in uploaded.name else ''
        if extension not in extensions:
            raise ValidationError(f'Format file tidak diizinkan. Gunakan: {", ".join(extensions).upper()}.')
        if uploaded.size > 2 * 1024 * 1024:
            raise ValidationError('Ukuran file maksimal 2 MB.')
        return uploaded

    def clean_cv(self):
        return self._validate_document('cv', {'pdf', 'doc', 'docx'})

    def clean_ijazah(self):
        return self._validate_document('ijazah', {'pdf', 'jpg', 'jpeg', 'png'})

    @transaction.atomic
    def save(self):
        nama = self.cleaned_data['nama_lengkap'].strip()
        parts = nama.split(maxsplit=1)
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else ''

        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=first_name,
            last_name=last_name,
        )

        profil = ProfilPelamar.objects.create(
            user=user,
            nik=self.cleaned_data['nik'],
            nomor_hp=self.cleaned_data['nomor_hp'],
            jenis_kelamin=self.cleaned_data['jenis_kelamin'],
            pendidikan_terakhir=self.cleaned_data['pendidikan_terakhir'],
            jurusan=self.cleaned_data['jurusan'].strip(),
            alamat=self.cleaned_data['alamat'].strip(),
        )

        DokumenPelamar.objects.create(
            profil=profil,
            cv=self.cleaned_data['cv'],
            ijazah=self.cleaned_data['ijazah'],
        )
        return profil
