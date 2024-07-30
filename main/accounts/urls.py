from django.urls import path
from .views import *


app_name = "accounts"
urlpatterns = [
    path('', index,name="index"),
    path('login/', user_login, name="user_login"),

    path('tum-kullanicilar/', all_user_list, name="all_user_list"),
    path('kullanici-ekle/', kuyumcu_kullanici_add, name="kuyumcu_kullanici_add"),
    path('kullanici-veri-ekle/<int:user_id>/', kullanici_veri_ekle, name="kullanici_veri_ekle"),

    path('kullanici-veri-duzenle/<int:veri_id>/', kullanici_veri_duzenle, name="kullanici_veri_duzenle"),
    path('kullanici-veri-sil/<int:veri_id>/', kullanici_veri_sil, name="kullanici_veri_sil"),
]
