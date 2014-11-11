# coding=utf-8
"""Model Admin Class."""

from django.contrib import admin

from wms_client.models import WMS


class WMSAdmin(admin.ModelAdmin):
    """Admin Class for User Model."""
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name', 'description']


admin.site.register(WMS, WMSAdmin)
