from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username",)


class FollowUserForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ["user"]
