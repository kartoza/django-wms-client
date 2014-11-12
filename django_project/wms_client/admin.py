# coding=utf-8
"""Model Admin Class."""

from django.contrib import admin
from wms_client.models.wms_resource import WMSResource


class WMSResourceAdmin(admin.ModelAdmin):
    """Admin Class for WMSResource Model."""
    exclude = ('slug',)
    list_display = ('name', 'uri', 'descriptions')
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(WMSResource, WMSResourceAdmin)
