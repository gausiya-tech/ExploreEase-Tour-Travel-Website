from django import forms
from django.core.validators import RegexValidator
from .models import Booking, Contact, Review, Feedback
class BookingForm(forms.ModelForm):
    mobile = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message="Enter a valid 10-digit Indian mobile number."
            )
        ]
    )
    class Meta:
        model = Booking
        fields = ["name", "email", "mobile", "address", "fromdate", "todate", "totalperson", "package"]
        widgets = {
            "fromdate": forms.DateInput(attrs={"type": "date"}),
            "todate": forms.DateInput(attrs={"type": "date"}),
        }
    def clean(self):
        cleaned = super().clean()
        start = cleaned.get("fromdate")
        end = cleaned.get("todate")

        if start and end and end <= start:
            self.add_error(
                "todate",
                "End date must be after start date."
            )

        return cleaned
class ContactForm(forms.ModelForm):

    mobile = forms.CharField(
        required=False,
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message="Enter a valid 10-digit Indian mobile number."
            )
        ]
    )

    class Meta:
        model = Contact
        fields = ["name", "email", "mobile", "message"]
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "email", "picture", "message"]
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "message"]
