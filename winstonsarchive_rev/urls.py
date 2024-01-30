"""
URL configuration for winstonsarchive_rev project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("amira/", include("amira.urls")),
    path("blog/", include("blog.urls")),
    path("api/", include("api.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
