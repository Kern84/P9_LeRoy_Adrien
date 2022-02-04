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
    list_user = models.User.objects.all()
    form = forms.UserFollowsForm()
    user = models.User.objects.get(id=request.user.id)

    if request.method == "POST":
        form = forms.UserFollowsForm(request.POST)
        input_user = request.POST["followed_user"]
        get_user = models.User.objects.get(username__exact=str(input_user))
        if str(input_user) in str(list_user):
            print("user ok")
            if form.is_valid():
                print("valid")
                follow_form = form.save(commit=False)
                follow_form.save()
                relation.user = get_user
                relation.followed_user = request.user
                relation.save()
                return redirect("subscription")
            else:
                print(form.errors.as_data())
        else:
            print("no user")

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
