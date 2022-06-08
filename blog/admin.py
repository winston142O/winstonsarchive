from django.contrib import admin
from .models import Post, Comment
from markdownx.admin import MarkdownxModelAdmin
from markdownx.admin import AdminMarkdownxWidget
from django.db import models

# Register your models here.

admin.site.register(Post)

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget}
    }

admin.site.register(Comment)