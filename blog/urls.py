from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url('', views.post_list, name='post_list'),
]