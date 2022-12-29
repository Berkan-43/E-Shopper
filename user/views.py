from django.shortcuts import render, redirect
from home.models import Setting
from product.models import *
from user.models import *
from user.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth  import update_session_auth_hash

# Create your views here.

def logout_view(request):
    logout(request)
    messages.success(request, 'başarıyla çıkış yapıldı.')
    return redirect ('home')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            current_user=request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="image/users/no-avatar.jpg"
            data.save()
            messages.success(request, 'Kaydınız Başarıyla  Oluşturuldu. Hesabınıza Erişmek için Giriş Yapın.')
            return redirect('login')
    else:
        form = UserForm()
    setting = Setting.objects.get(pk=1) 
    category = Category.objects.all()
    return render(request, 'register.html', context={
        'setting':setting,
        'category':category,
        'form':form
    })

@login_required(login_url='login')
def profile(request):
    setting = Setting.objects.get(pk=1) 
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    return render(request, 'profile.html', context={
        'setting':setting,
        'category':category,
        'profile':profile
    })


@login_required(login_url='login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance= request.user) # istek kullanıcının, kullanıcı oturum verileridir
        # "örnek = request.user.userprofile", 'userprofile' modelinden gelir -> OnetoOneField ilişkisi
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi.')
            return redirect('profile')

    else:
        category= Category.objects.all()
        current_user=request.user # Kullanıcı oturumu Bilgilerine Erişim
        user_form = UserUpdateForm(instance= request.user)
        profile_form= ProfileUpdateForm(instance= request.user.userprofile) # 'userprofile' modeli -> kullanıcıyla OnetoOneField ilişkisi
        
        return render(request, 'user_update.html', context={
            'category':category,
            'profile_form':profile_form,
            'user_form':user_form
        })


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Önemli
            messages.success(request, 'Şifreniz başarıyla yenilendi')
            return redirect('profile')
        else:
            messages.error(request, 'Birşeyler Yanlış gitti lütfen tekrar deneyin.<br>'+ str(form.errors))
            return redirect('change_password')
    else:
        category=Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', context={
            'form':form,
            'category':category
        })

