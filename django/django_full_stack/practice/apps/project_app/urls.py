from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/(?P<id>\d+)$', views.index),
    url(r'^reg_user$', views.reg_user),
    url(r'^login$', views.login),
    url(r'^yes$', views.dashboard),
    url(r'^add_message$', views.add_message),
    url(r'^logout$', views.logout),
    url(r'^show_message$', views.show_message),
    url(r'^delete/quote/(?P<id>\d+)$', views.delete)
    ]