"""
URL configuration for winstonsarchive_rev project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import (
    about_me
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("amira/", include("amira.urls")),
    path("blog/", include("blog.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("about-Winston/", about_me, name="about-Winston"),
    path("auth/", include("users.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)