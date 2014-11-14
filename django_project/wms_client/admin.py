# coding=utf-8
"""Model Admin Class."""

from django.contrib import admin
from wms_client.models.wms_resource import WMSResource


class WMSResourceAdmin(admin.ModelAdmin):
    """Admin Class for WMSResource Model."""
    exclude = ('slug',)
    list_display = ('name', 'uri')
    list_filter = ['name', 'uri']
    search_fields = ['name', 'description']

admin.site.register(WMSResource, WMSResourceAdmin)
