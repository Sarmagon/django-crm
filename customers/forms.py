from django import forms
from contracts.models import Contract
from leads.models import Lead
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("lead", "contract")

    def __init__(self, *args, lead_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["lead"].queryset = Lead.objects.filter(customer__isnull=True)
        self.fields["contract"].queryset = Contract.objects.filter(customer__isnull=True)
        if lead_id:
            self.fields["lead"].initial = lead_id
            self.fields["lead"].widget = forms.HiddenInput()
