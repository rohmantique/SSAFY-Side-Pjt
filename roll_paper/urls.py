from django.urls import path, include
from . import views

app_name = 'roll_paper'

urlpatterns = [ 
    path('index/', views.index, name='index'),
]