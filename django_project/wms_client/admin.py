# coding=utf-8
"""Model Admin Class."""

from django.contrib import admin

from wms_client.models import WMS
from wms_client.models.wms_resource import WMSResource


class WMSAdmin(admin.ModelAdmin):
    """Admin Class for User Model."""
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name', 'description']


class WMSResourceAdmin(admin.ModelAdmin):
    """Admin Class for WMSResource Model."""
    list_display = ('name', 'uri', 'descriptions')
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(WMS, WMSAdmin)

admin.site.register(WMSResource, WMSResourceAdmin)
