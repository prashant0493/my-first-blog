'''To add, delete and edit the blog post we need Django admin.'''
# Register your models here.

from django.contrib import admin
from .models import Post

admin.site.register(Post)

