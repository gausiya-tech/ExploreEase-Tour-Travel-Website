from django.db import models
from django.core.validators import MinValueValidator


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(upload_to="cities/", blank=True, null=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    title = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="packages")
    picture = models.ImageField(upload_to="packages/", blank=True, null=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    duration = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    address = models.TextField()
    fromdate = models.DateField()
    todate = models.DateField()
    totalperson = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    package = models.ForeignKey(Package, on_delete=models.PROTECT, related_name="bookings")
    total_amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.package_id:
            self.total_amount = self.package.price * self.totalperson

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.package.title}"

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    picture = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    picture = models.ImageField(upload_to="reviews/", blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name}"


class Team(models.Model):
    name = models.CharField(max_length=120)
    designation = models.CharField(max_length=120)
    picture = models.ImageField(upload_to="team/", blank=True, null=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"
