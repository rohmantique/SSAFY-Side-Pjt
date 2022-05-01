from django.contrib.auth.forms import UserChangeForm,UserCreationForm, AuthenticationForm, UsernameField
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
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
                'color': 'white',
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