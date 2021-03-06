# Generated by Django 4.0.1 on 2022-02-02 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_remove_user_followed_user_remove_user_following_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollows',
            name='followed_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userfollows',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
