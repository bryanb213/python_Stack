from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^wall$', views.display),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^message$', views.newMessage),
    url(r'^comment$', views.newComment),
    url(r'^delete/comment/(?P<id>\d+)$', views.deleteComment),
    url(r'^delete/message/(?P<id>\d+)$', views.deleteMessage),
    url(r'^edit_my_account/(?P<id>\d+)$', views.editMyAccount),
]