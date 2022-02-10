from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "role")


class Name(models.Model):
    followed_user = models.CharField(max_length=30)

    def __str__(self):
        return self.followed_user


class UserFollowsForm(ModelForm):
    class Meta:
        model = Name
        fields = [
            "followed_user",
        ]
        labels = {"followed_user": "Utilisateur à suivre :"}


class UnsubscribeForm(forms.Form):
    delete = forms.BooleanField(widget=forms.HiddenInput, initial=True)
