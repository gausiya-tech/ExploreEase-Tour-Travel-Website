from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Package, City, Gallery, Review, Team, Feedback
from .forms import BookingForm, ContactForm, ReviewForm, FeedbackForm

def home(request):
    packages = Package.objects.select_related("city").order_by("-id")[:6]
    cities = City.objects.all()[:6]
    return render(request, "tours/home.html", {"packages": packages, "cities": cities})


def package_list(request):
    packages = Package.objects.select_related("city").order_by("title")
    return render(request, "tours/packages.html", {"packages": packages})


def package_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, "tours/package_detail.html", {"package": package})


def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking request has been submitted.")
            return redirect("home")
    else:
        form = BookingForm()
    return render(request, "tours/form.html", {"form": form, "title": "Book a Tour"})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted.")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "tours/form.html", {"form": form, "title": "Contact Us"})


def gallery(request):
    items = Gallery.objects.all().order_by("-id")
    return render(request, "tours/gallery.html", {"items": items})


def reviews(request):
    items = Review.objects.all().order_by("-created_at")
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your review.")
            return redirect("reviews")
    else:
        form = ReviewForm()
    return render(request, "tours/reviews.html", {"items": items, "form": form})


def about(request):
    team = Team.objects.all()
    return render(request, "tours/about.html", {"team": team})
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your feedback.")
            return redirect("feedback")
    else:
        form = FeedbackForm()

    return render(
        request,
        "tours/form.html",
        {"form": form, "title": "Share Your Feedback"}
    )