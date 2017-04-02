"""ithehero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/(?P<slug>[\w\-]+)/$',blog, name='blog'),
    url(r'^blogs/$',blogs, name='blogs'),
    url(r'^exhibit/(?P<slug>[\w\-]+)/$',exhibit, name='exhibit'),
    url(r'^exhibits/$',exhibits, name='exhibits'),
    url(r'^exhibit/(?P<slugExhibit>[\w\-]+)/(?P<slugArt>[\w\-]+)/$',art, name='art'),
    url(r'^about/$',about, name='about'),
    url(r'^qr/$',qr, name='qr'),
    url(r'^project/(?P<slug>[\w\-]+)/$',project, name='project'),
    url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^filebrowser_filer/', include('ckeditor_filebrowser_filer.urls')),
    url(r'$', index, name="home")
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


