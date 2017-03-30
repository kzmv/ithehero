from django.contrib.admin import ModelAdmin, site
from .models import Blog, Exhibit, Art


class BlogAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ExhibitAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ArtAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

site.register(Blog, BlogAdmin)
site.register(Exhibit, ExhibitAdmin)
site.register(Art, ArtAdmin)