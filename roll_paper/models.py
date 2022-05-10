from django.db import models
from django.conf import settings
# Create your models here.

class RollPaper(models.Model):
    title = models.CharField(max_length = 35)
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