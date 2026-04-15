from django.contrib import admin
from django.urls import path, include

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
urlpatterns = [
    path("admin/", admin.site.urls),

    # tutte le API sotto /api/
    path("api/", include("GattiniCafe.urls")),

    #JWT
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]