from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import (
    CustomUserCreationForm, 
    CustomUserChangeForm,
    CustomPasswordRestForm
)
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

from .forms import (
    CustomAuthenticationForm, 
    CheckPasswordForm,
    CustomPasswordChangeForm,
)
from roll_paper.models import RollPaper
from accounts.models import User

from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


# Create your views here.

@require_http_methods(['GET', 'POST'])
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


@require_http_methods(['GET', 'POST'])
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
@require_http_methods(['GET', 'POST'])
def update(request):

    if request.method == 'POST':
        form1 = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = CheckPasswordForm(request.user, request.POST)
        if form1.is_valid():
            if password_form.is_valid():
                updated = form1.save(commit=False)
                my_sent_rollpaper = RollPaper.objects.filter(user2=request.user)
                for rollpaper in my_sent_rollpaper:
                    rollpaper.nickname = updated.nickname
                    rollpaper.save()
                updated.save()
                return redirect('rollpaper:index')

    else:
        form1 = CustomUserChangeForm(instance=request.user)
        password_form = CheckPasswordForm(request.user)

    context = {
        'form1': form1,
        'password_form': password_form
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form2 = CustomPasswordChangeForm(request.user, request.POST)
        if form2.is_valid():
            form2.save()
            update_session_auth_hash(request, form2.user)
            return redirect('accounts:update')
    else:
        form2 = CustomPasswordChangeForm(user=request.user)

    context = {
        'form2': form2,
    }
    return render(request, 'accounts/change_password.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def user_delete(request):

    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            return redirect('rollpaper:index')
    else:
        password_form = CheckPasswordForm(request.user)

    context = {
        'password_form': password_form,
    }

    return render(request, 'accounts/user_delete.html', context)


def forgot_id(request):

    if request.user.is_authenticated:
        return redirect('rollpaper:index')

    context = {

    }
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if user:
                template = render_to_string(
                    'accounts/email_template.html', 
                    { 'name':user.realname, 
                    'id':user.username,}
                    )
                send_email = EmailMessage(
                    '서울1반 추억쌓피 아이디 안내',
                    template,
                    'ddoongddangs@gmail.com',
                    [email],
                )
                send_email.send(fail_silently=False)
                return render(request, 'accounts/forgot_id_sent.html', context)
        except:
            messages.info(request, "해당 이메일의 사용자가 존재하지 않습니다.")
    return render(request, 'accounts/forgot_id.html', context)


def password_reset_complete(request):
    if request.user.is_authenticated:
        return redirect('rollpaper:index')
    return render(request, 'accounts/password_reset_complete.html')


class MyPasswordResetView(auth_views.PasswordResetView):
    success_url=reverse_lazy('accounts:password_reset_complete')
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_form.html'
    form_class = CustomPasswordRestForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('rollpaper:index')

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, { 'form': form })

    def form_valid(self, form):
        return super().form_valid(form)


class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url=reverse_lazy('accounts:login')
    template_name = 'accounts/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)
