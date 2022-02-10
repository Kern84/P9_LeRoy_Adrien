from django.db import IntegrityError
from django.forms import forms
from django.shortcuts import render, redirect
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
    list_user = models.User.objects.all()
    form = forms.UserFollowsForm()

    if request.method == "POST":
        if request.POST.get("role") == "add":
            form = forms.UserFollowsForm(request.POST)
            input_user = request.POST["followed_user"]
            try:
                get_user = models.User.objects.get(username__exact=str(input_user))
                if str(input_user) == str(request.user):
                    messages.error(request, "Soumission de formulaire invalide.")
                else:
                    if str(input_user) in str(list_user):
                        if form.is_valid():
                            relation = models.UserFollows(
                                user=request.user, followed_user=get_user
                            )
                            relation.save()
                            return redirect("subscription")
            except (AttributeError, ObjectDoesNotExist, IntegrityError):
                messages.error(request, "Soumission de formulaire invalide.")
                messages.error(request, form.errors)

        elif request.POST.get("role") == "delete":
            subscriber_id = request.POST.get("sub_id")
            subscriber_to_unfollow = models.UserFollows.objects.filter(
                user=request.user
            ).get(followed_user=subscriber_id)
            if subscriber_to_unfollow:
                subscriber_to_unfollow.delete()
                return redirect("subscription")

    followings = models.UserFollows.objects.filter(user=request.user)
    subscriber = [following.followed_user for following in followings]
    subscription = models.UserFollows.objects.filter(followed_user=request.user)

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
