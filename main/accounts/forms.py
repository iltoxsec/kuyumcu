from django import forms
from django.contrib.auth.models import User
from .models import KuyumcuKullanicilar


class KuyumcuKullanicilarYeniKullaniciForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
    
    def save(self, commit=True):
        user = super(KuyumcuKullanicilarYeniKullaniciForm, self).save(commit=False)
        if not user.username:
            user.username = (user.first_name + user.last_name).lower().replace(' ', '') + str(User.objects.count() + 1)
        if commit:
            user.save()
        return user


class KuyumcuKullanicilarForm(forms.ModelForm):
    tarih = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    class Meta:
        model = KuyumcuKullanicilar
        fields = ['tip', 'cins', 'miktar', 'milyem_per_cm', 'birim', 'alt_toplam', 'aciklama', 'adet', 'iscilik', 'mm_per_cm', 'isc_toplam', 'islem_tipi', 'tarih']
