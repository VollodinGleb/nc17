"""conf URL Configuration

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
from django.urls import re_path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.urls import resolve


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += i18n_patterns(
    re_path(r'^', include('content.urls', namespace='content')),
    re_path(r'^rosetta/', include('rosetta.urls')),
)

# include redirect patterns after all others are registered
urlpatterns += [
    re_path(r'^$', RedirectView.as_view(pattern_name='content:home', permanent=False))
]