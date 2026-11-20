from django.contrib import admin
from .models import City, Package, Booking, Contact, Gallery, Review, Team, Feedback


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "price", "duration", "date")
    list_filter = ("city", "date")
    search_fields = ("title", "city__name")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "package", "fromdate", "todate", "totalperson", "total_amount", "created_at")
    list_filter = ("fromdate", "package")
    search_fields = ("name", "email", "mobile")
    readonly_fields = ("total_amount", "created_at")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "mobile", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "message")
    readonly_fields = ("created_at",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "designation")
    search_fields = ("name", "designation")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)
