from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


"""    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = ((SUBSCRIBER, "Abonné"),)

    profile_photo = models.ImageField(verbose_name="photo de profil")
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="Rôle")
"""
