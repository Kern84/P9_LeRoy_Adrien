# Generated by Django 4.0.1 on 2022-01-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_user_profile_photo_remove_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('SUBSCRIBER', 'Abonné')], default='SUBSCRIBER', max_length=30, verbose_name='Rôle'),
            preserve_default=False,
        ),
    ]
