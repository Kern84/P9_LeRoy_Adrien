# Generated by Django 4.0.1 on 2022-01-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_remove_user_following_user_userfollows_followed_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(to='authentication.UserFollows'),
        ),
    ]
