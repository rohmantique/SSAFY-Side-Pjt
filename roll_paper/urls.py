from django.urls import path, include
from . import views

app_name = 'rollpaper'

urlpatterns = [ 
    path('index/', views.index, name='index'),
    path('userlst/', views.userlst, name='userlst'),
    path('write/<int:user_pk>/', views.write, name='write'),
    path('<int:rollpaper_pk>/', views.detail, name='detail'),
    path('<int:rollpaper_pk>/update/', views.update, name='update'),

]