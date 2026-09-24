from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ("last_name", "first_name", "phone", "email", "advertisement")
