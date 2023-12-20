from django.urls import path
from .views import SentenceListView

urlpatterns = [
    path('sentences', SentenceListView.as_view(), name='api-sentence-list'),
]
