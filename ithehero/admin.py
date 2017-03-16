from django.contrib.admin import ModelAdmin, site
from .models import Blog


class BlogAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


site.register(Blog, BlogAdmin)