from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Blog(models.Model):

    CATEGORIES = (('a','Article'),('p','Project'),('b','About'),('i',"Intro"))
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255)
    text = RichTextField()
    description = RichTextField(default="")
    date = models.DateField()
    user = models.ForeignKey(User)

    language = models.CharField(max_length=2,choices=[("en","English"), ("bg","Bulgarian")])
    published = models.BooleanField(default=True)
    category = models.CharField(max_length=1, choices=CATEGORIES, default='a')
    image = models.ImageField(upload_to="images",default="images/noimage.jpg")


    def __str__(self):
        return self.title

class Exhibit(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255)
    description = RichTextField(default="")
    info = RichTextField()
    image = models.ImageField(upload_to="images",default="images/noimage.jpg")

    def __str__(self):
        return self.title

class Art(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company = models.ImageField(upload_to="images",default="images/noimage.jpg")
    game = models.ImageField(upload_to="images",default="images/noimage.jpg")
    slug = models.SlugField(unique=True, max_length=255)
    story = RichTextField()
    info = RichTextField()
    stats = RichTextField(default="")
    picture = models.ImageField(upload_to="images",default="images/noimage.jpg")
    audio = models.FileField(upload_to ="audio", default="audio/default.mp3")

    def __str__(self):
        return self.title