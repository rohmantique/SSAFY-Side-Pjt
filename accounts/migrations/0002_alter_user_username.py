# Generated by Django 3.2.12 on 2022-05-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': '이미 존재하는 아이디입니다.'}, max_length=10, unique=True, verbose_name='username'),
        ),
    ]