from django.contrib import admin
from .models import Post, Tag
from amira.models import Sentence

admin.site.register((Post, Tag))