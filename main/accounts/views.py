from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q

def index(request):
    return render(request, 'accounts/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            return HttpResponse('Invalid login details.')
    return render(request, 'accounts/login.html')



def all_user_list(request):
    query = request.GET.get('q')
    if query:
        users = KuyumcuKullanicilar.objects.filter(
            Q(name__icontains=query) |
            Q(tip__icontains=query) |
            Q(cins__icontains=query) |
            Q(miktar__icontains=query) |
            Q(milyem_per_cm__icontains=query) |
            Q(birim__icontains=query) |
            Q(alt_toplam__icontains=query) |
            Q(aciklama__icontains=query) |
            Q(adet__icontains=query) |
            Q(iscilik__icontains=query) |
            Q(mm_per_cm__icontains=query) |
            Q(isc_toplam__icontains=query)
        )
    else:
        users = User.objects.all()

    return render(request, 'accounts/user_list.html', {'users': users})

def kuyumcu_kullanici_add(request):
    if request.method == 'POST':
        form = KuyumcuKullanicilarYeniKullaniciForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('accounts:kullanici_veri_ekle', user_id=new_user.id)
    else:
        form = KuyumcuKullanicilarYeniKullaniciForm()
        users = User.objects.all()
    
    context = {
        'users': users,
        'form': form
    }
    return render(request, 'accounts/kullanici_add.html', context)


def kullanici_veri_ekle(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = KuyumcuKullanicilarForm(request.POST)
        if form.is_valid():
            kuyumcu_kullanici = form.save(commit=False)
            kuyumcu_kullanici.user = user
            kuyumcu_kullanici.save()
            return redirect('accounts:kullanici_veri_ekle', user_id=user_id)
    else:
        form = KuyumcuKullanicilarForm()
    return render(request, 'accounts/kullanici_veri_ekle.html', {'form': form, 'user': user})


def kullanici_veri_duzenle(request, veri_id):
    veri = get_object_or_404(KuyumcuKullanicilar, id=veri_id)
    if request.method == 'POST':
        form = KuyumcuKullanicilarForm(request.POST, instance=veri)
        if form.is_valid():
            form.save()
            return redirect('accounts:kullanici_veri_ekle', user_id=veri.user.id)
    else:
        form = KuyumcuKullanicilarForm(instance=veri)
    return render(request, 'accounts/kullanici_veri_duzenle.html', {'form': form, 'veri': veri})

def kullanici_veri_sil(request, veri_id):
    veri = get_object_or_404(KuyumcuKullanicilar, id=veri_id)
    user_id = veri.user.id
    veri.delete()
    return redirect('accounts:kullanici_veri_ekle', user_id=user_id)