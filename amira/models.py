from django.db import models

class Sentence(models.Model):
    sentence = models.CharField(max_length=500, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sentence