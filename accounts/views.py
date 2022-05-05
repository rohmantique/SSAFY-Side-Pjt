from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm, 
    PasswordChangeForm
)
from .forms import (
    CustomUserCreationForm, 
    CustomUserChangeForm
)
from django.contrib import messages
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    get_user_model,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import CustomAuthenticationForm, CheckPasswordForm

# Create your views here.
def signup(request):

    if request.user.is_authenticated:
        return redirect('rollpaper:index')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('rollpaper:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form
    }

    return render(request, 'accounts/signup.html', context)

def login(request):

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():

            user = form.get_user()
            auth_login(request, user)

            next_url = request.GET.get('next')

            return redirect(next_url or 'rollpaper:main')

    else:
        form = CustomAuthenticationForm()

    context = {
        'form':form,
    }
        
    return render(request, 'accounts/login.html', context)

@login_required
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('rollpaper:index')

@login_required
def update(request):

    if request.method == 'POST':
        form1 = CustomUserChangeForm(request.POST, instance=request.user)
        if form1.is_valid():
            form1.save()
            return redirect('rollpaper:index')
    else:
        form1 = CustomUserChangeForm(instance=request.user)

    context = {
        'form1': form1,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form2 = PasswordChangeForm(request.user, request.POST)
        if form2.is_valid():
            form2.save()
            update_session_auth_hash(request, form2.user)
            return redirect('accounts:update')
    else:
        form2 = PasswordChangeForm(user=request.user)

    context = {
        'form2': form2,
    }
    return render(request, 'accounts/change_password.html', context)

@login_required
def user_delete(request):

    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, '회원탈퇴가 완료되었습니다!')
            return redirect('accounts:signup')
    else:
        password_form = CheckPasswordForm(request.user)

    context = {
        'password_form': password_form,
    }

    return render(request, 'accounts/user_delete.html', context)



