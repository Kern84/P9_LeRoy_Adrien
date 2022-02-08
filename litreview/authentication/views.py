from gettext import install
from django.db import IntegrityError
from django.forms import forms
from django.shortcuts import render, redirect, get_object_or_404
from authentication import forms, models
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "authentication/signup.html", context={"form": form})


@login_required
def subscriptions(request):
    relation = models.UserFollows()
    list_user = models.User.objects.all()
    form = forms.UserFollowsForm()

    if request.method == "POST":
        form = forms.UserFollowsForm(request.POST)
        input_user = request.POST["followed_user"]
        try:
            get_user = models.User.objects.get(username__exact=str(input_user))
            if str(input_user) in str(list_user):
                if form.is_valid():
                    relation.user = get_user
                    relation.followed_user = request.user
                    relation.save()
                    return redirect("subscription")
        except (AttributeError, ObjectDoesNotExist, IntegrityError):
            messages.error(request, "Soumission de formulaire invalide.")
            messages.error(request, form.errors)

    if models.UserFollows.objects.all():
        subscriber = models.UserFollows.objects.all()
    else:
        subscriber = "Pas d'abonnements"
    if models.UserFollows.objects.all():
        subscription = models.UserFollows.objects.all()[0].followed_user.username
    else:
        subscription = "Pas d'abonnés"

    context = {
        "form": form,
        "subscriber": subscriber,
        "subscription": subscription,
    }

    return render(
        request,
        "authentication/subscription.html",
        context=context,
    )


@login_required
def unfollow(request, sub_id):
    get_subscriber = get_object_or_404(models.UserFollows, id=sub_id)
    unsubscribe_form = forms.UnsubscribeForm()
    if request.method == "POST":
        if "delete" in request.POST:
            unsubscribe_form = forms.UnsubscribeForm(request.POST)
            if unsubscribe_form.is_valid():
                get_subscriber.delete()
                return redirect("subscription")
    context = {
        "unsubscribe_form": unsubscribe_form,
        "get_subscriber": get_subscriber,
    }
    return render(
        request,
        "authentication/delete_sub.html",
        context=context,
    )
