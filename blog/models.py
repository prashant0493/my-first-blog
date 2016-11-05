# Create your models here.
from django.db import models            # django.db should be database related module
from django.utils import timezone      #django.utils should be utility ralted module

class Post(models.Model):                   # Post is name of our model/class. Attributes are:-->>[author, title, text, created_date, published_date]
                                           # models.Model means that Post is a Django model and Django knows it should be saved in Database.
    author=models.ForeignKey('auth.user')  # This is link to another model.         
    title=models.CharField(max_length=200) # Text with limited number of characters...since, Title should not have many characters.
    text=models.TextField()                # Long text without limit. 
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)

def publish(self):
    self.published_date=timezone.now()
    self.save()

def __str__(self):
    return self.title
    
