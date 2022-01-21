from django.forms import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms, models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    return render(
        request,
        "publication/home.html",
        context={"tickets": tickets, "reviews": reviews},
    )


"""    reviews = models.Review.objects.filter(user__in=request.user.all())
    tickets = models.Ticket.objects.filter(
        user__in=request.user.all()
    )  # .exclude(review__in=reviews)
    context = {
        "reviews": reviews,
        "tickets": tickets,
    }
    return render(request, "publication/home.html", context=context)
"""


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("home")
    return render(request, "publication/create_ticket.html", context={"form": form})


@login_required
def create_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("home")
    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }
    return render(request, "publication/create_review.html", context=context)


@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, "publication/view_review.html", {"review": review})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == "POST":
        if "edit_review" in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect("home")
        if "delete_review" in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect("home")
    context = {
        "edit_form": edit_form,
        "delete_form": delete_form,
    }
    return render(request, "publication/edit_review.html", context=context)


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == "POST":
        if "edit_ticket" in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect("home")
        if "delete_ticket" in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect("home")
    context = {
        "edit_form": edit_form,
        "delete_form": delete_form,
    }
    return render(request, "publication/edit_ticket.html", context=context)
