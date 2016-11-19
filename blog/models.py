# Create your models here.
# After each change to models.py, first 'makemigrations' and secondly 'migrate'
from django.db import models            # django.db should be database related module
from django.utils import timezone      #django.utils should be utility ralted module

class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


def publish(self):
    self.published_date=timezone.now()
    self.save()

def __str__(self):
    return self.title

