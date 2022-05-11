from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    realname = models.CharField(
        max_length=8, 
        blank=False, 
        unique=True,
        error_messages={
            'unique': "이미 존재하는 이름입니다.",
        }
        )
    nickname = models.CharField(max_length=10, blank=False, unique=True,
        error_messages={
            'unique': "이미 존재하는 닉네임입니다.",
        }
    )
    # 오류메시지 username -> '아이디'로 수정
    username = models.CharField(
        ('username'),
        max_length=10,
        unique=True,
        error_messages={
            'unique': "이미 존재하는 아이디입니다.",
        },
    )