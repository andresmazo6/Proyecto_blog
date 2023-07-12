from django.db import models
from oauth2_provider.models import AbstractApplication

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Aplication(AbstractApplication):
    pass