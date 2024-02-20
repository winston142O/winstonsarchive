from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title  = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts')
    likes = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '{} - {}'.format(self.post.title, self.created_by, self.body)