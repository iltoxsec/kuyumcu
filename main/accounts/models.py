from django.db import models
from django.urls import reverse


class KuyumcuKullanicilar(models.Model):
    STATUS = [
        ('Altın verildi', 'Altın verildi'),
        ('Altın Alındı!', 'Altın Alındı!'),
        ('İşlem Yok', 'İşlem Yok'),
    ]
    user = models.ForeignKey('auth.User', verbose_name='Author',
                             related_name='kuyumcu_kullanicilar', on_delete=models.CASCADE)
    tip = models.CharField(max_length=100)
    cins = models.CharField(max_length=100)
    miktar = models.DecimalField(max_digits=10, decimal_places=2)
    milyem_per_cm = models.DecimalField(max_digits=10, decimal_places=2)
    birim = models.CharField(max_length=10)
    alt_toplam = models.DecimalField(max_digits=10, decimal_places=2)
    aciklama = models.TextField()
    adet = models.IntegerField()
    iscilik = models.DecimalField(max_digits=10, decimal_places=2)
    mm_per_cm = models.CharField(max_length=10)
    isc_toplam = models.DecimalField(max_digits=10, decimal_places=2)
    islem_tipi = models.CharField(default="Test", choices=STATUS, max_length=30)
    tarih = models.DateTimeField(
        verbose_name="Tarih")


    def __str__(self):
        return self.name
