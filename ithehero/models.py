from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Blog(models.Model):
    
    text = RichTextField()
    date = models.DateField()
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=2,choices=[("en","English"), ("bg","Bulgarian")])

    def __str__(self):
        return self.title

    def get_slug(self):
        return slugify(self.title)

    