from django.db import models
from django.conf import settings
from django.core.validators import BaseValidator
# Create your models here.

class RollPaper(models.Model):
    title = models.CharField(
        max_length = 35,
        blank=False,
        error_messages={
            'max_length': '제목이 35글자 이내인지 확인해주세요',
        }
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
    
# class MaxLengthValidator(BaseValidator):
#     message = ngettext_lazy(
#         'Ensure this value has at most %(limit_value)d character (it has %(show_value)d).',
#         'Ensure this value has at most %(limit_value)d characters (it has %(show_value)d).',
#         'limit_value')
#     code = 'max_length'

# class wordCloud(models.Model):
#     content = models.CharField(max_length=10)