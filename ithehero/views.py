from django.shortcuts import render
from .models import Blog

def index(request):
    blog = Blog.objects.first()
    return render(request, 'index.html', {'blog': blog.text})