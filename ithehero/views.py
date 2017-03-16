from django.shortcuts import render
from .models import Blog

def index(request):

    return render(request, 'en/index.html')

def blogs(request):
    blogs = Blog.objects.filter(published=True)
    print(blogs)
    return render(request, 'en/blogs.html', {'blogs': blogs})

def blog(request,slug):
    blog = Blog.objects.filter(published=True,slug=slug)[0]
    return render(request, 'en/blog.html', {'blog': blog})