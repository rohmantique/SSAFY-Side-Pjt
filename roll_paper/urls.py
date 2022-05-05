from django.urls import path
from . import views

app_name = 'rollpaper'

urlpatterns = [ 
    path('', views.index, name='index'),
    path('rollpaper/main/', views.main, name='main'),
    path('rollpaper/userlst/', views.userlst, name='userlst'),
    path('rollpaper/aboutus/', views.aboutus, name='aboutus'),

    #편지쓰기
    path('rollpaper/write/<str:realname>/', views.write, name='write'),
    path('rollpaper/complete/', views.complete, name='complete'),

    #편지읽기
    path('rollpaper/<int:user_pk>/letterbox/', views.letterbox, name='letterbox'),
    path('rollpaper/<int:user_pk>/letterbox/<int:rollpaper_pk>/', views.detail, name='detail'),

    #편지수정 & 삭제
    path('rollpaper/sentletter/<int:user_pk>/', views.sentletter, name='sentletter'),
    path('rollpaper/sentletter/<int:user_pk>/<str:realname>/', views.update, name='update'),
    path('rollpaper/sentletter/<int:user_pk>/<str:realname>/delete/', views.delete, name='delete'),
]