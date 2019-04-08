from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^quotes$', views.quotes),
    url(r'new_quote$', views.new_quote),
    url(r'^add_favorite/(?P<number>\d+)$', views.add_favorite),
    url(r'^delete/(?P<number>\d+)$', views.delete),
    url(r'^users/(?P<number>\d+)$', views.view_user),
    url(r'^editpage/(?P<number>\d+)', views.editpage),
    url(r'^edit_account/(?P<number>\d+)$', views.edit_account),
]