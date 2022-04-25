from django.db import models

# Create your models here.

class User(models.Model):
    email = models.TextField(null=False)
    password = models.CharField(max_length=20, null=False)
    fullname = models.CharField(max_length=3, null=False)
    nickname = models.CharField(max_length=20, null=False)
