from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.display),
    url(r'^reg_user$', views.reg_user),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add_quote$', views.add_quote),
    url(r'^add_comment$', views.add_comment),
    url(r'^delete/comment/(?P<id>\d+)$', views.delete_comment),
    url(r'^delete/message/(?P<id>\d+)$', views.delete_message),
    url(r'^edit_account/(?P<id>\d+)$', views.edit_account),
]