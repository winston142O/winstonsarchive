from django.urls import path
from .views import (
    SentenceListView,
    SentenceCreateView,
    ValentinesView,
    APISentenceListView
)

urlpatterns = [
    path('IsTheLoveOfMyLife', SentenceListView.as_view(), name='ily_amira'),
    path('BeMyValentine', ValentinesView, name='valentine_amira'),
    path('create-msg/', SentenceCreateView.as_view(), name='create_sentence'),
    path('api/sentences', APISentenceListView.as_view(), name='api-sentence-list'),
]