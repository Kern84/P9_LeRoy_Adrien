from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings


class User(AbstractUser):

    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = ((SUBSCRIBER, "Abonné"),)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="Rôle")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.SUBSCRIBER:
            group = Group.objects.get(name="subscribers")
            group.user_set.add(self)


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = (
            "user",
            "followed_user",
        )
