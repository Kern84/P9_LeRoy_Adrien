# Generated by Django 4.0.1 on 2022-02-03 15:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_alter_user_following_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following_user',
            field=models.ManyToManyField(blank=True, related_name='follows', through='authentication.UserFollows', to=settings.AUTH_USER_MODEL, verbose_name='suivre'),
        ),
    ]
