from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm, 
    AuthenticationForm, 
    UsernameField,
    PasswordChangeForm,
)
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    realname = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'realname',
                'data-bs-toggle': 'tooltip',
                'data-bs-placement': 'top',
            }
        )
    )
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            }),
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control'
            }),
        strip=False,
    )    
    class Meta:
        model = User
        fields = ('username','realname','nickname','password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )    
    password = None

    class Meta:
        model = User
        fields = ('nickname',)


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                }),
    )
    password = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control'}),
    )

class ChangePasswordForm(PasswordChangeForm):
    password1=forms.CharField(
        label='기존 비밀번호',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control',
            }
        )
    
    )
    newpassword1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    newpassword2 = forms.CharField(
        label='새 비밀번호 (확인)',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = None

    class Meta:
        model = User
        fields = ('password1', 'newpassword1', 'newpassword2',)

    

class CheckPasswordForm(forms.Form):
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 
                }
        ),
    )
    def __init__(self, user, *args, **kwargs): #현재 접속중인 사용자의 password 가져오기 위해 init 메서드로 user객체 생성
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self): #clean 메서드로 form에 입력된 password값과 init으로 생성된 현재 사용자의 password 값을 check_password 통해 비교
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
