from django.test import TestCase
from django.urls import reverse
from datetime import date, timedelta

from .models import City, Package, Booking, Feedback
from .forms import FeedbackForm


class ExploreEaseBackendTests(TestCase):

    def setUp(self):
        self.city = City.objects.create(name="Test City")
        self.package = Package.objects.create(
            title="Test Tour",
            city=self.city,
            price=5000,
            duration="3 Days",
            details="Test package details",
            date=date.today()
        )

    def test_package_creation(self):
        self.assertEqual(self.package.title, "Test Tour")
        self.assertEqual(self.package.price, 5000)

    def test_booking_amount_calculation(self):
        booking = Booking.objects.create(
            name="Test User",
            email="test@example.com",
            mobile="9876543210",
            address="Test Address",
            fromdate=date.today() + timedelta(days=5),
            todate=date.today() + timedelta(days=8),
            totalperson=2,
            package=self.package
        )
        self.assertEqual(booking.total_amount, 10000)

    def test_feedback_form_valid(self):
        form = FeedbackForm(data={
            "name": "Test User",
            "email": "test@example.com",
            "message": "Good website"
        })
        self.assertTrue(form.is_valid())

    def test_feedback_submission(self):
        response = self.client.post(
            reverse("feedback"),
            {
                "name": "Test User",
                "email": "test@example.com",
                "message": "Good website"
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Feedback.objects.count(), 1)
