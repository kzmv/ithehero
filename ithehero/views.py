from django.shortcuts import render
from .models import Blog

def index(request):
    articles = Blog.objects.filter(published=True,category="a")
    projects = Blog.objects.filter(published=True,category="p")

    return render(request, 'en/index.html',{'articles': articles, 'projects': projects})

def blogs(request):
    blogs = Blog.objects.filter(published=True,category="a")
    projects = Blog.objects.filter(published=True,category="p")

    print(blogs)
    return render(request, 'en/blogs.html', {'blogs': blogs, 'projects': projects})

def blog(request,slug):
    blog = Blog.objects.filter(published=True,slug=slug)[0]
    projects = Blog.objects.filter(published=True,category="p")
    return render(request, 'en/blog.html', {'blog': blog, 'projects': projects})

def about(request):
    blogs = Blog.objects.filter(published=True,category="b")
    projects = Blog.objects.filter(published=True,category="p")
    return render(request, 'en/about.html', {'blogs': blogs, 'projects': projects})


def project(request,slug):
    blog = Blog.objects.filter(published=True,slug=slug)[0]
    projects = Blog.objects.filter(published=True,category="p")

    return render(request, 'en/project.html', {'blog': blog, 'projects': projects})