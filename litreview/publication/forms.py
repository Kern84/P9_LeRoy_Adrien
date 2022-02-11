from django import forms
from . import models


class TicketForm(forms.ModelForm):
    """Class for the creation of a ticket."""

    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]
        labels = {"title": "Titre"}


RATINGS = [("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)]


class ReviewForm(forms.ModelForm):
    """Class for the creation of a review."""

    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    note = forms.ChoiceField(widget=forms.RadioSelect, choices=RATINGS)

    class Meta:
        model = models.Review
        fields = ["headline", "note", "body"]
        labels = {"headline": "Titre", "note": "Note", "body": "Commentaire"}


class DeleteForm(forms.Form):
    """Class for the deletion of a ticket or review."""

    delete = forms.BooleanField(widget=forms.HiddenInput, initial=True)
