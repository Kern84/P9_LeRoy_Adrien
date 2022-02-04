from turtle import textinput
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import UserFollows, User


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "role")


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ["user", "followed_user"]
        labels = {"followed_user": "Utilisateur à suivre :"}
        exclude = ["user"]
        widgets = {"followed_user": forms.TextInput}


class Unsubscribe(forms.Form):
    unsubscribe = forms.BooleanField(widget=forms.HiddenInput, initial=True)
