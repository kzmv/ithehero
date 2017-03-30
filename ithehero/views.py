from django.shortcuts import render

from .models import *

def index(request):
    intro = Blog.objects.filter(published=True,category="i")[0]
    articles = Blog.objects.filter(published=True,category="a")
    projects = Blog.objects.filter(published=True,category="p")

    return render(request, 'en/index.html',{'articles': articles, 'projects': projects,'intro':intro})

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

def qr(request):
    return render(request, 'en/qr.html')

def exhibits(request):
    exhibits = Exhibit.objects.all()
    projects = Blog.objects.filter(published=True,category="p")

    return render(request, 'en/exhibits.html', {'exhibits': exhibits, 'projects': projects})

def exhibit(request, slug):
    exhibit = Exhibit.objects.filter(slug=slug)[0]
    projects = Blog.objects.filter(published=True,category="p")
    arts = Art.objects.filter(exhibit=exhibit)

    return render(request, 'en/exhibit.html', {'exhibit': exhibit,'arts':arts, 'projects': projects})

def art(request, slugExhibit, slugArt):
    exhibit = Exhibit.objects.filter(slug=slugExhibit)[0]
    art = Art.objects.filter(exhibit=exhibit,slug=slugArt)
    projects = Blog.objects.filter(published=True,category="p")

    return render(request, 'en/art.html', {'exhibit': exhibit,'art':art, 'projects': projects})