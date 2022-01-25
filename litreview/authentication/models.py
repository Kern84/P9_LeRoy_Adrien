from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = ((SUBSCRIBER, "Abonné"),)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="Rôle")

    # follows = models.ManyToManyField(
    #    "UserFollows", symmetrical=False, verbose_name="suivre"
    # )
    following_user = models.ManyToManyField(
        "self",
        symmetrical=False,
        verbose_name="suivre",
    )
    # followed_user = models.ManyToManyField(
    #    "self", symmetrical=False, verbose_name="suivi par"
    # )


"""class UserFollows(models.Model):
    following_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    class Meta:
        unique_together = (
            "following_user",
            "followed_user",
        )
"""
