from django.contrib import admin
from .models import Post, Tag, Comment

admin.site.register((Post, Tag, Comment))