from django.http import HttpResponse
from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_safe, require_GET
from django.contrib.auth import get_user_model

from roll_paper.models import RollPaper
from accounts.models import User

from .forms import RollPaperForm

# Create your views here.
@require_safe
def index(request):
    if request.user.is_authenticated:
        return redirect('rollpaper:main')
    return render(request, 'roll_paper/index.html')

@require_GET
def main(request):
    return render(request, 'roll_paper/main.html')

@require_GET
def aboutus(request):
    return render(request, 'roll_paper/aboutus.html')


@login_required
@require_GET
def userlst(request):
    user_lst = User.objects.all().order_by('realname')
    excepted = []

    for user in user_lst[:]:
        person = RollPaper.objects.filter(user2=request.user, user=user)
        if person:
            excepted.append(user)
    
    empty = 0
    if len(user_lst)-1 == len(excepted):
        empty = 1

    context = {
        'user_lst': user_lst,
        'excepted' : excepted,
        'empty' : empty
    }
    return render(request, 'roll_paper/user_lst.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def write(request, realname):
    receiver = get_object_or_404(get_user_model(), realname=realname)
   
    if request.method == 'POST':
        form = RollPaperForm(request.POST)
        if form.is_valid():
            rollpaper = form.save(commit=False)
            rollpaper.user = receiver
            rollpaper.user2 = request.user
            rollpaper.save()

            return redirect('rollpaper:complete')

    else:
        if request.user == receiver:
            return redirect('rollpaper:userlst')

        form = RollPaperForm()

    context = {
        'form': form,
    }
    return render(request, 'roll_paper/write.html', context)

def complete(request):
    return render(request, 'roll_paper/complete.html')

@login_required
@require_GET
def letterbox(request, user_pk):
    receiver = get_object_or_404(get_user_model(), pk=user_pk)

    if receiver == request.user:
        user_info = request.user
        my_rollpaper = RollPaper.objects.filter(user=request.user)
        number = len(my_rollpaper)
        context = {
            'my_rollpaper': my_rollpaper,
            'user_info': user_info,
            'number':number,
            'realname': user_info.realname[1:],
        }
        return render(request, 'roll_paper/letterbox.html', context)
    return render(request, 'roll_paper/error.html')


@login_required
@require_GET
def detail(request, user_pk, rollpaper_pk):
    receiver = get_object_or_404(get_user_model(), pk=user_pk)
    rollpaper = get_object_or_404(RollPaper, pk=rollpaper_pk)

    if rollpaper.user == receiver:
        context = {
            'rollpaper': rollpaper,
            'from' : rollpaper.user2.nickname
        }
        return render(request, 'roll_paper/detail.html', context)
    return render(request, 'roll_paper/error.html')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, user_pk, realname):
    writer = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user == writer:
        receiver = get_object_or_404(get_user_model(), realname=realname)
        rollpaper = get_object_or_404(RollPaper, user = receiver, user2 = request.user)

        if request.method == 'POST':
            form = RollPaperForm(request.POST, instance=rollpaper)
            if form.is_valid():
                rollpaper = form.save()
                return redirect('rollpaper:sentletter', user_pk)
        else:
            form = RollPaperForm(instance=rollpaper)

        context = {
            'form': form,
            'realname' : realname
        }

        return render(request, 'roll_paper/update.html', context)
    return render(request, 'roll_paper/error.html')


@login_required
@require_GET
def sentletter(request, user_pk):
    writer = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user == writer:
        user_info = request.user
        sentrollpaper = RollPaper.objects.filter(user2=request.user)
        context = {
            'sentrollpaper': sentrollpaper,
            'user_info': user_info
        }
        return render(request, 'roll_paper/sentletter.html', context)
    return render(request, 'roll_paper/error.html')


@login_required
@require_http_methods(['POST'])
def delete(request, user_pk, realname):
    
    if not request.user.is_authenticated:
        return HttpResponse('권한이 없습니다', status=401)

    receiver = get_object_or_404(get_user_model(), realname=realname)
    sentrollpaper = RollPaper.objects.filter(user = receiver, user2=request.user)
    sentrollpaper.delete()
    messages.add_message(request, messages.ERROR, '편지가 성공적으로 삭제되었습니다! 감성의 추진력을 얻기 위함인가요?')
    return redirect('rollpaper:sentletter', user_pk)