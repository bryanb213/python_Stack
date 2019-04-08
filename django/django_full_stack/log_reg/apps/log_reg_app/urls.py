from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register$', views.reg_user),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add_message$', views.add_message)
]