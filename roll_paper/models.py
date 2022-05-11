from django.db import models
from django.conf import settings

# from django.core.validators import BaseValidator
# Create your models here.

class RollPaper(models.Model):
    title = models.CharField(
        max_length = 35,
        blank=False,
        )
    content = models.TextField()
    nickname = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='receiver'
    )

    user2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='sender'
    )

# 수정중
# class FixedLengthValidator(BaseValidator):
#     message = "제목이 최대 35글자인지 확인해주세요."