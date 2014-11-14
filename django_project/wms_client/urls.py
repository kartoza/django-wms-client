# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'wms_client.views.index', name='index'),
    url(r'^map/(?P<slug>[\w-]+)/$', 'wms_client.views.map', name='map'),
)
