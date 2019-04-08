from django.conf.urls import url
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$',views.authors),
    url(r'^books/(?P<id>\d+)$', views.showbook),
    url(r'^author_page/(?P<id>\d+)$', views.showauthor),
    url(r'^addbook$', views.addbook),
    url(r'^addauthor$', views.addauthor),
    url(r'^addauthor_tobook/(?P<id>\d+)$', views.addauthor_tobooks),
    url(r'^addbook_toauthor/(?P<id>\d+)$', views.addbook_toauthors), 
]