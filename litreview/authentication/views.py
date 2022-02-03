from django.forms import forms
from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth import login
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
    relation = models.UserFollows()
    user = models.User.objects.get(id=request.user.id)
    if models.UserFollows.objects.all():
        subscriber = models.UserFollows.objects.all()
    else:
        subscriber = "Pas d'abonnements"
    if models.UserFollows.objects.all():
        subscription = models.UserFollows.objects.all()[0].followed_user.username
    else:
        subscription = "Pas d'abonnés"
    form = forms.UserFollowsForm(instance=request.user)
    if request.method == "POST":
        form = forms.UserFollowsForm(request.POST, instance=request.user)
        if form.is_valid():
            follow_form = form.save(commit=False)
            follow_form.save()
            relation.user = request.user
            relation.followed_user = request.user
            relation.save()
            # follow_form.followed_user.add(request.user)
            # form.save_m2m()
            return redirect("subscription")
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
