from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Post(models.Model):
    title  = models.CharField(max_length=150)
    content = MarkdownxField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def formatted(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = MarkdownxField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '{} - {}'.format(self.post.titulo, self.name, self.body)