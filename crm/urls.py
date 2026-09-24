from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("users.urls")),
    path("products/", include("products.urls")),
    path("ads/", include("ads.urls")),
    path("leads/", include("leads.urls")),
    path("contracts/", include("contracts.urls")),
    path("customers/", include("customers.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
