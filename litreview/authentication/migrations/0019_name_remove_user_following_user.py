# Generated by Django 4.0.1 on 2022-02-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0018_user_following_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_user', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='following_user',
        ),
    ]
