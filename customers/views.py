from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from leads.models import Lead
from .forms import CustomerForm
from .models import Customer


class CustomerListView(PermissionRequiredMixin, ListView):
    model = Customer
    permission_required = "customers.view_customer"
    context_object_name = "customers"
    template_name = "customers/customers-list.html"


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    permission_required = "customers.add_customer"
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("customers:list")

    def dispatch(self, request, *args, **kwargs):
        self.lead_id = request.GET.get("lead") or request.POST.get("lead")
        if self.lead_id:
            get_object_or_404(Lead.objects.filter(customer__isnull=True), pk=self.lead_id)
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["lead_id"] = self.lead_id
        return kwargs


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    model = Customer
    permission_required = "customers.view_customer"
    template_name = "customers/customers-detail.html"


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    permission_required = "customers.change_customer"
    template_name = "customers/customers-edit.html"

    def get_success_url(self):
        return reverse_lazy("customers:detail", kwargs={"pk": self.object.pk})


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Customer
    permission_required = "customers.delete_customer"
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy("customers:list")
