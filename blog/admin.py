'''To add, delete and edit the blog post we need Django admin.'''
# Register your models here.

# To make sure, models visible on admin page we have to register them on admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)

