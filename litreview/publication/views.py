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
