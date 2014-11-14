# coding=utf-8
"""Model class for WMS Resource"""
__author__ = 'ismailsunni'
__project_name = 'django-wms-client'
__filename = 'wms_resource.py'
__date__ = '11/11/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.contrib.gis.db import models
from django.conf.global_settings import MEDIA_ROOT
from django.utils.text import slugify
import os
from owslib.wms import WebMapService, ServiceException, CapabilitiesError


class WMSResource(models.Model):
    """WMS Resource model."""

    zoom_lookup = [360.0 / 2**i for i in range(20)]

    class Meta:
        """Meta class."""
        app_label = 'wms_client'

    slug = models.SlugField(
        unique=True,
        primary_key=True
    )

    name = models.CharField(
        help_text='The identifier for the WMS Resource.',
        null=False,
        blank=False,
        unique=True,
        max_length=100
    )

    uri = models.CharField(
        help_text='URI for the WMS resource',
        null=False,
        blank=False,
        max_length=100
    )

    layers = models.CharField(
        help_text='The layers that you want to retrieve.',
        blank=True,
        null=False,
        max_length=100,
    )

    descriptions = models.TextField(
        help_text='This is similar to abstract part of a wms resources.',
        blank=True,
    )

    preview = models.ImageField(
        help_text='Preview image for this WMS Resource.',
        upload_to=os.path.join(MEDIA_ROOT, 'wms_preview'),
        blank=True
    )

    zoom = models.IntegerField()

    min_zoom = models.IntegerField()

    max_zoom = models.IntegerField(default=19)

    north = models.FloatField()
    east = models.FloatField()
    south = models.FloatField()
    west = models.FloatField()

    def center_south(self):
        return sum([self.north, self.south]) / 2

    def center_east(self):
        return sum([self.north, self.south]) / 2

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Overloaded save method."""
        try:
            self.populate_wms_resource()
        except ValueError:
            # If the URI is not valid.
            self.descriptions += ' This Uri probably is not valid.'
        except (ServiceException, CapabilitiesError):
            # If there is an error, use the value from user.
            pass
        self.slug = slugify(unicode(self.name))
        if not self.layers:
            self.layers = self.name
        super(WMSResource, self).save(*args, **kwargs)

    def populate_wms_resource(self):
        """Populate the model fields based on a uri."""
        wms = WebMapService(self.uri)
        self.name = wms.identification.title
        self.descriptions = wms.identification.abstract
        if self.layers:
            layer_name = self.layers[0]  # Take the first layer.
            bounding_box_wgs84 = wms.contents[layer_name].boundingBoxWGS84

            self.north = bounding_box_wgs84[3]
            self.east = bounding_box_wgs84[0]
            self.south = bounding_box_wgs84[1]
            self.east = bounding_box_wgs84[2]
            self.min_zoom = self.get_min_zoom()
            self.zoom = self.min_zoom

        else:
            return

    def get_min_zoom(self):
        length_north_south = abs(self.north - self.south)
        length_east_west = abs(self.east - self.west)

        length_map = max(length_north_south, length_east_west)

        i = 0
        while length_map < self.zoom_lookup[i] and i < 19:
            i += 1

        # Get the closest zoom
        if (abs(length_map - self.zoom_lookup[i]) <
                abs(length_map - self.zoom_lookup[i - 1])):
            return i
        else:
            return i - 1
