from django.urls import path
from .import views

app_name = 'accounts'
urlpatterns = [ 
    # 회원가입, 로그인 및 로그아웃
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # 회원정보 수정
    path('update/', views.update, name='update'),
    path('change_password/', views.change_password, name='change_password'),

    # 회원탈퇴
    path('user_delete/', views.user_delete, name='user_delete'),

    # 아이디, 비밀번호 찾기
    path('forgot_id/', views.forgot_id, name='forgot_id')
        
]