from django.urls import reverse
from .models import Sentence
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
import os

# Create your views here.

class SentenceListView(ListView):
    model = Sentence
    template_name = 'amira/amira_home.html' 
    context_object_name = 'sentences'
    
    # Get images from static folder
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        months = ['dec_2022', 'jan_2023', 'feb_2023', 'mar_2023', 'apr_2023', 'may_2023', 'jun_2023', 'jul_2023', 'aug_2023', 'sep_2023', 'oct_2023', 'nov_2023', 'dec_2023']

        images_by_month = {}
        base_folder = 'static/css/amira/imgs/us/'

        for month in months:
            folder_path = os.path.join(base_folder, month)
            images_by_month[month] = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

        context['images_by_month'] = images_by_month
        return context
    
    ordering = ['-date_added']

class SentenceCreateView(CreateView):
    model = Sentence
    fields = ['sentence']
    template_name = 'amira/create_sentence.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('create_sentence')