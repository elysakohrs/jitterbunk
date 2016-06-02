from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.user, name='user'),
    url(r'^(?P<user_id>[0-9]+)/bunk$', views.bunk, name='bunk'),
]