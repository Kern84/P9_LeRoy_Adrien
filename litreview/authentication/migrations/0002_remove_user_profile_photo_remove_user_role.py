# Generated by Django 4.0.1 on 2022-01-19 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
