from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("packages/", views.package_list, name="packages"),
    path("packages/<int:pk>/", views.package_detail, name="package_detail"),
    path("booking/", views.booking_create, name="booking"),
    path("contact/", views.contact, name="contact"),
    path("gallery/", views.gallery, name="gallery"),
    path("reviews/", views.reviews, name="reviews"),
    path("about/", views.about, name="about"),
    path("feedback/", views.feedback, name="feedback"),
]
