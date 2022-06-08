from unicodedata import name
from django import forms
from .models import Comment
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from matplotlib import widgets
from django.db import models
from markdownx.widgets import MarkdownxWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
        widgets = {
            'body': models.TextField()
        }
        
        formfield_overrides = {
            models.TextField: {'widget': MarkdownxWidget},
        }