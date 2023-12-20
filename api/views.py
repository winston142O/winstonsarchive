from django.shortcuts import render
from rest_framework import generics
from amira.models import Sentence
from .serializers import SentenceSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@permission_classes([AllowAny])
class SentenceListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
