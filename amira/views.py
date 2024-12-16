from django.urls import reverse
from .models import Sentence
from .serializers import SentenceSerializer
from django.views.generic import (
    ListView, 
    CreateView,
)
import os
from dotenv import load_dotenv
from datetime import timedelta
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.mixins import UserPassesTestMixin


# Load environment variables from .env file
load_dotenv()

class SentenceListView(UserPassesTestMixin, ListView):
    model = Sentence
    template_name = 'amira/amira_home.html' 
    context_object_name = 'sentences'
    
    # Only allow certain users
    def test_func(self):
        allowed_users = os.getenv('ALLOWED_USERS', '').split(',')
        return self.request.user.username in allowed_users

    # Redirect is user is not allowed
    def handle_no_permission(self):        
        messages.warning(self.request, 'You do not have access to this part of the site...')
        return redirect('profile')
    
    # Get images from static folder
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # TODO: Make this dynamic
        months = [
            'dec_2022',
            'jan_2023',
            'feb_2023',
            'mar_2023',
            'apr_2023',
            'may_2023',
            'jun_2023',
            'jul_2023',
            'aug_2023',
            'sep_2023',
            'oct_2023',
            'nov_2023',
            'dec_2023'
        ] # TODO: Update pictures

        images_by_month = {}
        base_folder = 'static/css/amira/imgs/us/'

        # Accepted file types
        file_types = ('.png', '.jpg', '.jpeg')

        for month in months:
            folder_path = os.path.join(base_folder, month)
            if os.path.exists(folder_path):
                images_by_month[month] = [file for file in os.listdir(folder_path) if file.lower().endswith(file_types)]
            else:
                images_by_month[month] = []

        context['images_by_month'] = images_by_month
        return context
    
    ordering = ['-date_added']

class SentenceCreateView(UserPassesTestMixin, CreateView):    
    model = Sentence
    fields = ['sentence']
    template_name = 'amira/create_sentence.html'
    
    # Only allow certain users
    def test_func(self):
        allowed_users = config('ALLOWED_USERS').split(',')
        return self.request.user.username in allowed_users

    # Redirect if user is not allowed
    def handle_no_permission(self):
        messages.error(self.request, 'You do not have access to this part of the site...')
        return redirect('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('create_sentence')
    
def ValentinesView(request):
    return render(request, 'amira/valentines.html')

@permission_classes([AllowAny])
class APISentenceListView(generics.ListAPIView):
    """
    Allows retrieving all sentences.
    """
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer
