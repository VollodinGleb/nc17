from django.urls import re_path
from .views import *
from django.utils.translation import gettext_lazy as _

app_name = 'content'

urlpatterns = [
    re_path(_(r'^$'), HomeView.as_view(), name='home'),
    re_path(_(r'about/$'), AboutView.as_view(), name='about'),
    re_path(r'photos/$', PhotosView.as_view(), name='photos'),
    re_path(r'videos/$', VideosView.as_view(), name='videos'),
    re_path(r'contacts/$', ContactsView.as_view(), name='contacts'),
    re_path(r'promotions/(?P<slug>[\w-]+)/$', PromotionsView.as_view(), name='promotions'),
]
