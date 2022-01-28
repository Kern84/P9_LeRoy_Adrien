from django.forms import forms
from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings


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
    subscriber = models.User.objects.filter(following_user__username=request.user)
    subscription = models.User.objects.filter(
        user__in=request.user.following_user.all()
    )
    form = forms.FollowUserForm(instance=request.user)
    unsubscribe_form = forms.Unsubscribe()
    if request.method == "POST":
        form = forms.FollowUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("subscription")
        if "unsubscribe" in request.POST:
            unsubscribe_form = forms.Unsubscribe(request.POST)
            if unsubscribe_form.is_valid():
                subscriber.delete()
                return redirect("subscription")
    context = {
        "subscriber": subscriber,
        "subscription": subscription,
        "form": form,
        "unsubscribe_form": unsubscribe_form,
    }
    return render(
        request,
        "authentication/subscription.html",
        context=context,
    )
