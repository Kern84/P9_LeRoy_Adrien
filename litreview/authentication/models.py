from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = ((SUBSCRIBER, "Abonné"),)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="Rôle")


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )

    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    def __str__(self):
        return self.followed_user.username

    class Meta:
        unique_together = (
            "user",
            "followed_user",
        )
