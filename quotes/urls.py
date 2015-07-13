from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^api/all/$', views.quotes_as_json, name='all_json'),
    url(r'^feed/all/$', views.LatestQuotesFeed(), name='all_feed'),
]
