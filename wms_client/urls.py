# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'wms_client.views.index', name='index'),
    url(r'^users.json', 'wms_client.views.get_users', name='get_users'),

    url(r'^register$', 'wms_client.views.register', name='register'),
    url(r'^account-confirmation/(?P<uid>[0-9A-Za-z_\-]+)/(?P<key>.+)/$',
        'wms_client.views.confirm_registration',
        name='confirm_registration'),

    url(r'^login$', 'wms_client.views.login', name='login'),
    url(r'^logout$', 'wms_client.views.logout', name='logout'),
    url(r'^update-profile$', 'wms_client.views.update_user', name='update_user'),
    url(r'^delete-user$', 'wms_client.views.delete_user', name='delete_user'),

    url(r'^password-reset/$', 'wms_client.views.password_reset',
        name='password_reset'),
    url(r'^password-reset/done/$', 'wms_client.views.password_reset_done',
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        'wms_client.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        'wms_client.views.password_reset_complete',
        name='password_reset_complete'),

    url(r'^download$', 'wms_client.views.download', name='download'),
)
