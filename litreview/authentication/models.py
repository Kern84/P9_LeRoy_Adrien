from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserFollows(models.Model):
    users = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="suivi",
    )

    class Meta:
        unique_together = (
            "users",
            "followed_user",
        )


class User(AbstractUser):

    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = ((SUBSCRIBER, "Abonné"),)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="Rôle")

    following_user = models.ManyToManyField(
        "self",
        symmetrical=False,
        verbose_name="suivre",
    )

    follows = models.ManyToManyField(UserFollows)
