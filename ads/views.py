from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import AdvertisementForm
from .models import Advertisement


class AdvertisementListView(PermissionRequiredMixin, ListView):
    model = Advertisement
    permission_required = "ads.view_advertisement"
    context_object_name = "ads"
    template_name = "ads/ads-list.html"


class AdvertisementCreateView(PermissionRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    permission_required = "ads.add_advertisement"
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("ads:list")


class AdvertisementDetailView(PermissionRequiredMixin, DetailView):
    model = Advertisement
    permission_required = "ads.view_advertisement"
    template_name = "ads/ads-detail.html"


class AdvertisementUpdateView(PermissionRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    permission_required = "ads.change_advertisement"
    template_name = "ads/ads-edit.html"

    def get_success_url(self):
        return reverse_lazy("ads:detail", kwargs={"pk": self.object.pk})


class AdvertisementDeleteView(PermissionRequiredMixin, DeleteView):
    model = Advertisement
    permission_required = "ads.delete_advertisement"
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("ads:list")


class AdvertisementStatisticsView(PermissionRequiredMixin, ListView):
    model = Advertisement
    permission_required = "ads.view_advertisement"
    context_object_name = "ads"
    template_name = "ads/ads-statistic.html"

    def get_queryset(self):
        advertisements = Advertisement.objects.annotate(
            leads_count=Count("leads", distinct=True),
            customers_count=Count("leads__customer", distinct=True),
            contracts_total=Sum("leads__customer__contract__cost"),
        )
        for advertisement in advertisements:
            advertisement.profit = (
                advertisement.contracts_total / advertisement.budget
                if advertisement.contracts_total is not None and advertisement.budget else None
            )
        return advertisements
