from django import forms
from .models import Post
from django.db import models
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': CKEditorWidget(),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }        