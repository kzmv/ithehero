from django.contrib.admin import ModelAdmin, site
from .models import Blog


class BlogAdmin(ModelAdmin):
    pass

site.register(Blog, BlogAdmin)