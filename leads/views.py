from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import LeadForm
from .models import Lead


class LeadListView(PermissionRequiredMixin, ListView):
    model = Lead
    permission_required = "leads.view_lead"
    context_object_name = "leads"
    template_name = "leads/leads-list.html"


class LeadCreateView(PermissionRequiredMixin, CreateView):
    model = Lead
    form_class = LeadForm
    permission_required = "leads.add_lead"
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("leads:list")


class LeadDetailView(PermissionRequiredMixin, DetailView):
    model = Lead
    permission_required = "leads.view_lead"
    template_name = "leads/leads-detail.html"


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    model = Lead
    form_class = LeadForm
    permission_required = "leads.change_lead"
    template_name = "leads/leads-edit.html"

    def get_success_url(self):
        return reverse_lazy("leads:detail", kwargs={"pk": self.object.pk})


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    model = Lead
    permission_required = "leads.delete_lead"
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("leads:list")
