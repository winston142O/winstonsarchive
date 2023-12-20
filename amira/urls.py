from django.urls import path

from .views import (
    SentenceListView,
    SentenceCreateView
)

urlpatterns = [
    path('IsTheLoveOfMyLife', SentenceListView.as_view(), name='ily_amira'),
    path('create-msg/', SentenceCreateView.as_view(), name='create_sentence'),
]