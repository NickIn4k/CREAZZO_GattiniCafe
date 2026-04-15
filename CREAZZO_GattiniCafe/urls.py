from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # tutte le API sotto /api/
    path("api/", include("GattiniCafe.urls")),
]