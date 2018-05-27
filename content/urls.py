from django.conf.urls import url
from .views import *
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    url(_(r'^$'), HomeView.as_view(), name='home'),
    url(_(r'about/$'), AboutView.as_view(), name='about'),
    url(r'photos/$', PhotosView.as_view(), name='photos'),
    url(r'videos/$', VideosView.as_view(), name='videos'),
    url(r'contacts/$', ContactsView.as_view(), name='contacts'),
    url(r'promotions/(?P<slug>[\w-]+)/$', PromotionsView.as_view(), name='promotions'),
]
