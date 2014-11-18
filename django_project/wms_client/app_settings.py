# coding=utf-8
"""Settings file for WMS Client.

"""
from django.conf import settings


# Allow base django project to override settings
default_leaflet_tiles = (
    'OpenStreetMap',
    'http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
    ('© <a href="http://www.openstreetmap.org" target="_parent">OpenStreetMap'
     '</a> and contributors, under an <a '
     'href="http://www.openstreetmap.org/copyright" target="_parent">open '
     'license</a>')
)
LEAFLET_TILES = getattr(settings, 'LEAFLET_TILES', default_leaflet_tiles)

settings.TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.media',
)
