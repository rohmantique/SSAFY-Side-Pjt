from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User

# Create your views here.
def signup(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        fullname = request.POST.get('fullname')
        nickname = request.POST.get('nickname')

        user = User()
        user.email = email
        user.password = password
        user.fullname = fullname
        user.nickname = nickname
        user.save()

        return redirect('accounts:login')

    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # 안써도 됨
        # fullname = request.POST['fullname']
        # nickname = request.POST['nickname']
        user = auth.authenticate(request, email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('roll_paper:index')
        else:
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')
