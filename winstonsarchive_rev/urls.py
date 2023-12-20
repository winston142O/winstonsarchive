"""
URL configuration for winstonsarchive_rev project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("amira/", include("amira.urls")),
    path("api/", include("api.urls")),
]
