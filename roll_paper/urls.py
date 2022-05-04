from django.urls import path
from . import views

app_name = 'rollpaper'

urlpatterns = [ 
    path('index/', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('userlst/', views.userlst, name='userlst'),

    #편지쓰기
    path('write/<str:realname>/', views.write, name='write'),
    path('complete/', views.complete, name='complete'),

    #편지읽기
    path('<int:user_pk>/letterbox/', views.letterbox, name='letterbox'),
    path('<int:user_pk>/letterbox/<int:rollpaper_pk>/', views.detail, name='detail'),

    #편지수정 & 삭제
    path('sentletter/<int:user_pk>/', views.sentletter, name='sentletter'),
    path('sentletter/<int:user_pk>/<str:realname>/', views.update, name='update'),
    path('sentletter/<int:user_pk>/<str:realname>/delete/', views.delete, name='delete'),


]