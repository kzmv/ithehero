from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Blog(models.Model):
    
    text = RichTextField()
    date = models.DateField()
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=2,choices=[("en","English"), ("bg","Bulgarian")])
    published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.title

    