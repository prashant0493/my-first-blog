from django.shortcuts import render    # This file serves requests from the user. Hence, business logic lies here
from django.http import HttpResponse

# render would put together out entire template
# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

