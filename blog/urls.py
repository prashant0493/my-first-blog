# Last part name='index' is the name of the view
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index')
    ]
