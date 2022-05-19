from django.urls import path
from django.urls import reverse_lazy
from .import views
from django.contrib.auth import views as auth_views

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

    # 아이디 찾기, 비밀번호 재설정
    path('forgot_id/', views.forgot_id, name='forgot_id'),
    
    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', 
        views.MyPasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"), 
        name='password_reset_confirm'),
    path('reset_complete/', views.password_reset_complete, name='password_reset_complete')
        
]
