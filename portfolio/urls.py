from django.urls import path
from .views import (
    portfolio
)

urlpatterns = [
    path("", portfolio, name="portfolio"),
]