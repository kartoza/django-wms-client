from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^wms_client/', include('wms_client.urls', namespace='wms_client'))
)
