from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import ContractForm
from .models import Contract


class ContractListView(PermissionRequiredMixin, ListView):
    model = Contract
    permission_required = "contracts.view_contract"
    context_object_name = "contracts"
    template_name = "contracts/contracts-list.html"


class ContractCreateView(PermissionRequiredMixin, CreateView):
    model = Contract
    form_class = ContractForm
    permission_required = "contracts.add_contract"
    template_name = "contracts/contracts-create.html"
    success_url = reverse_lazy("contracts:list")


class ContractDetailView(PermissionRequiredMixin, DetailView):
    model = Contract
    permission_required = "contracts.view_contract"
    template_name = "contracts/contracts-detail.html"


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    permission_required = "contracts.change_contract"
    template_name = "contracts/contracts-edit.html"

    def get_success_url(self):
        return reverse_lazy("contracts:detail", kwargs={"pk": self.object.pk})


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    model = Contract
    permission_required = "contracts.delete_contract"
    template_name = "contracts/contracts-delete.html"
    success_url = reverse_lazy("contracts:list")
