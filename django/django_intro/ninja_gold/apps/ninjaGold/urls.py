from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.home),
    url(r'^process_money$', views.process),
    url(r'^clear$', views.clear)
    ]