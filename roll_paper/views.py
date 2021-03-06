from django.http import HttpResponse
from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_safe, require_GET
from django.contrib.auth import get_user_model

from roll_paper.models import RollPaper
from accounts.models import User

from .forms import RollPaperForm

from datetime import datetime

# 워드클라우드
# from wordcloud import WordCloud
# from collections import Counter
# from konlpy.tag import Okt
# from PIL import Image
# import numpy as np

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
    now = datetime.now()
    target_day = datetime(year=2022, month=5, day=28, hour=23, minute=59, second=59)
    if now < target_day:    
        user_lst = User.objects.all().order_by('realname')
        currentuser = len(user_lst) - 1
        excepted = []

        for user in user_lst:
            person = RollPaper.objects.filter(user2=request.user, user=user)
            if person:
                excepted.append(user)
        
        empty = 0
        if len(user_lst)-1 == len(excepted):
            empty = 1

        context = {
            'user_lst': user_lst,
            'excepted' : excepted,
            'empty' : empty,
            'currentuser' : currentuser,
            'targetday': target_day,
        }
        return render(request, 'roll_paper/user_lst.html', context)
    else:
        name = request.user.realname[-2:]
        context = {
            'name': name,
        }
        return render(request, 'roll_paper/user_lst_disable.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def write(request, realname):
    receiver = get_object_or_404(get_user_model(), realname=realname)
   
    if request.method == 'POST':
        paperform = RollPaperForm(request.POST)
        if paperform.is_valid():
            rollpaper = paperform.save(commit=False)
            rollpaper.nickname = request.user.nickname
            rollpaper.user = receiver
            rollpaper.user2 = request.user
            rollpaper.save()

            return redirect('rollpaper:complete')

    else:
        if request.user == receiver:
            return redirect('rollpaper:userlst')

        paperform = RollPaperForm()

    context = {
        'paperform': paperform,
        'receiver': realname[-2:]
    }
    return render(request, 'roll_paper/write.html', context)

def complete(request):
    return render(request, 'roll_paper/complete.html')


@login_required
@require_GET
def letterbox(request, user_pk):

    if request.user.pk == user_pk:
        now = datetime.now()
        target_day = datetime(year=2022, month=5, day=27, hour=0, minute=0, second=0)
        if now > target_day:

            # # 워드클라우드
            # with open('wordcloud.txt', 'r', encoding='utf-8') as f:
            #     text = f.read()

            # okt = Okt()
            # morphs = okt.morphs(text)

            # words = [n for n in morphs if len(n) > 1]

            # c = Counter(words)

            # img = Image.open('./static/clover.jpeg')
            # img_array = np.array(img)

            # wc = WordCloud(
            #     font_path='static/css/BMHANNA_11yrs_ttf.ttf', 
            #     width=800, height=800, scale=0.8, 
            #     max_font_size=100, 
            #     background_color="white", 
            #     mask=img_array
            #     ).generate_from_frequencies(c)
            # wc.to_file('./static/wordcloud.jpg')

            # 편지함
            user_info = request.user
            my_rollpaper = RollPaper.objects.filter(user=request.user)
            number = len(my_rollpaper)
            context = {
                'my_rollpaper': my_rollpaper,
                'user_info': user_info,
                'number':number,
                'realname': user_info.realname[-2:],
            }
            return render(request, 'roll_paper/letterbox.html', context)

        else:
            d_day = target_day - now
            context = {
                'targetday': target_day,
                'dday': d_day,
            }
            return render(request, 'roll_paper/letterbox_disable.html', context)

    return render(request, 'roll_paper/error.html')


@login_required
@require_GET
def detail(request, user_pk, rollpaper_pk):
    rollpaper = get_object_or_404(RollPaper, pk=rollpaper_pk)

    if rollpaper.user.pk == user_pk:
        context = {
            'rollpaper': rollpaper,
            'from' : rollpaper.nickname
        }
        return render(request, 'roll_paper/detail.html', context)
    return render(request, 'roll_paper/error.html')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, user_pk, realname):
    if request.user.pk == user_pk:
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
    now = datetime.now()
    target_day = datetime(year=2022, month=5, day=26, hour=23, minute=59, second=59)
    if now < target_day:    
        if request.user.pk == user_pk:
            sentrollpaper = RollPaper.objects.filter(user2=request.user)
            realname = []
            for rollpaper in sentrollpaper:
                if rollpaper.user:
                    realname.append(rollpaper.user.realname)
            realname.sort()
            context = {
                'realname' : realname
            }
            return render(request, 'roll_paper/sentletter.html', context)
        return render(request, 'roll_paper/error.html')
    else:
        name = request.user.realname[-2:]
        context = {
            'name': name,
        }
        return render(request, 'roll_paper/write_disable.html', context)        


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