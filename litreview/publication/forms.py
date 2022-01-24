from dataclasses import fields
from django import forms
from django.contrib.auth import get_user_model
from . import models


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]


class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ["headline", "rating", "body"]


class DeleteForm(forms.Form):
    delete = forms.BooleanField(widget=forms.HiddenInput, initial=True)
