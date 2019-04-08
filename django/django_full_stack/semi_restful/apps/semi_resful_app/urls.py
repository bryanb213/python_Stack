from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows/new$', views.index),
    url(r'^shows/create$', views.addshow),
    url(r'^shows$', views.allshows),
    url(r'^shows/(?P<id>\d+)$', views.show_shows),
    url(r'^shows/(?P<id>\d+)/edit$', views.editshow),
    url(r'^shows/(?P<id>\d+)/update$', views.update),
    url(r'^shows/(?P<id>\d+)/destroy$', views.delete)
]