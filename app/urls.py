from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^query/$', views.query, name='query'),
    url(r'^sign/(?P<pk>[0-9]+)/$', views.sign, name='sign'),
]
