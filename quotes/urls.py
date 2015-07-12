from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^api/all/$', views.quotes_as_json, name='all_json'),
]
