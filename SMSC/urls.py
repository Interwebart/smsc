from django.conf.urls import include, url
from SMSC import views

#Django site authentication urls (for login, logout, password management)





urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^account/$', views.account, name='account'),
    url(r'^billing/$', views.billing, name='billing'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^ndb/$', views.ndb, name='ndb'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

]