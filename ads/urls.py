from django.urls import path
from .views import (
    AdvertisementCreateView, AdvertisementDeleteView, AdvertisementDetailView,
    AdvertisementListView, AdvertisementStatisticsView, AdvertisementUpdateView,
)

app_name = "ads"
urlpatterns = [
    path("", AdvertisementListView.as_view(), name="list"),
    path("new/", AdvertisementCreateView.as_view(), name="create"),
    path("statistic/", AdvertisementStatisticsView.as_view(), name="statistic"),
    path("<int:pk>/", AdvertisementDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", AdvertisementUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", AdvertisementDeleteView.as_view(), name="delete"),
]
