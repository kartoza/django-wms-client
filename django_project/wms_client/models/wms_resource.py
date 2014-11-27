    # coding=utf-8
"""Model class for WMS Resource"""
__author__ = 'ismailsunni'
__project_name = 'django-wms-client'
__filename = 'wms_resource.py'
__date__ = '11/11/14'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''


import os
from django.contrib.gis.db import models
from django.conf.global_settings import MEDIA_ROOT
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import random
from owslib.wms import WebMapService, ServiceException, CapabilitiesError
import urllib
import imghdr

import logging
logger = logging.getLogger(__name__)


class WMSResource(models.Model):
    """WMS Resource model."""

    zoom_lookup = [360.0 / 2 ** i for i in range(20)]

    class Meta:
        """Meta class."""
        app_label = 'wms_client'

    slug = models.SlugField(
        unique=True,
        primary_key=True
    )

    name = models.CharField(
        help_text='A name for the WMS map.',
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

    layers = models.TextField(
        help_text=(
            'The layers to be included in the map. Separate with commas, '
            'no spaces between the commas. If left blank the top of '
            'the layer list tree will be used by default.'),
        blank=True,
        null=False,
    )

    description = models.TextField(
        help_text=(
            'Description for the map. If left blank, the WMS abstract text '
            'will be used.'),
        blank=True,
    )

    preview = models.ImageField(
        help_text='Preview image for this WMS Resource.',
        upload_to=os.path.join(MEDIA_ROOT, 'wms_preview'),
        blank=True
    )

    zoom = models.IntegerField(
        help_text='Default zoom level (1-19) for this map.',
        blank=True,
        validators=[
            MaxValueValidator(19),
            MinValueValidator(0)
        ]
    )

    min_zoom = models.IntegerField(
        help_text='Default minimum zoom level (0-19) for this map.',
        blank=True,
        validators=[
            MaxValueValidator(19),
            MinValueValidator(0)
        ],
        null=True
    )

    max_zoom = models.IntegerField(
        help_text=(
            'Default minimum zoom level (0-19) for this map. Defaults to 19'),
        blank=True,
        default=19,
        validators=[
            MaxValueValidator(19),
            MinValueValidator(0)
        ],
        null=True
    )

    north = models.FloatField(
        help_text=(
            'Northern boundary in decimal degrees. Will default to maxima '
            'of all layers.'),
        blank=True,
        null=True
    )
    east = models.FloatField(
        help_text=(
            'Eastern boundary in decimal degrees. Will default to maxima '
            'of all layers.'),
        blank=True,
        null=True
    )
    south = models.FloatField(
        help_text=(
            'Southern boundary in decimal degrees. Will default to minima '
            'of all layers.'),
        blank=True,
        null=True
    )
    west = models.FloatField(
        help_text=(
            'Western boundary in decimal degrees. Will default to minima '
            'of all layers.'),
        blank=True,
        null=True
    )

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
        # except ValueError:
        #     # If the URI is not valid.
        #     if 'This Uri probably is not valid.' not in self.description:
        #         self.description += ' This Uri probably is not valid.'
        except (ServiceException, CapabilitiesError):
            # If there is an error, use the value from user.
            pass
        if not self.slug:
            self.slug = slugify(unicode(self.name))

        # Populate preview
        # noinspection PyBroadException
        try:
            if not self.preview:
                self.populate_preview()
        except Exception as e:
            logger.info('Failed to populate preview, %s' % e)

        super(WMSResource, self).save(*args, **kwargs)

    def populate_wms_resource(self):
        """Populate the model fields based on a uri."""
        wms = WebMapService(self.uri)
        if not self.name:
            self.name = wms.identification.title
        if not self.description:
            self.description = wms.identification.abstract

        # If empty, set to all layers available
        if not self.layers:
            self.layers = ','.join(wms.contents.keys())

        if self.layers:
            north = []
            east = []
            south = []
            west = []

            layers = self.layers.split(',')
            for layer in layers:
                try:
                    bounding_box_wgs84 = wms.contents[layer].boundingBoxWGS84
                except KeyError:
                    continue

                north.append(bounding_box_wgs84[3])
                east.append(bounding_box_wgs84[2])
                south.append(bounding_box_wgs84[1])
                west.append(bounding_box_wgs84[0])

            # Do not set if they have been set.
            if not self.north:
                self.north = max(north)
            if not self.east:
                self.east = max(east)
            if not self.south:
                self.south = min(south)
            if not self.west:
                self.west = min(west)

        if self.min_zoom is None or self.min_zoom < self.get_min_zoom():
            self.min_zoom = self.get_min_zoom()

        if self.zoom is None:
            self.zoom = self.min_zoom
        # Zoom must be in the min/max range
        if self.zoom < self.min_zoom:
            self.zoom = self.min_zoom
        if not self.max_zoom:
            self.max_zoom = 19

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

    def populate_preview(self):
        """Return thumbnail for preview image."""
        wms = WebMapService(self.uri)

        # Get layers
        # noinspection PyBroadException
        try:
            layers = self.layers.split(',')
        except:
            layers = None
        # Get random layer if not specified
        if not layers:
            layers = [random.choice(list(wms.contents))]

        srs = 'EPSG:4326'
        size = (300, 300)
        bbox = (self.west, self.south, self.east, self.north)
        image_formats = wms.getOperationByName('GetMap').formatOptions
        image_format = 'image/jpeg'
        if image_format in image_formats:
            pass
        elif len(image_formats) > 0:
            image_format = image_formats[0]
        else:
            raise OSError

        image = None
        styles = []

        try:
            image = self.retrieve_map_owslib(
                self.uri, bbox, srs, size, image_format, styles, layers, wms)
        except Exception as e:
            logger.info('Failed to use retrieve_map_owslib, %s' % e)

        if not image:
            try:
                image = self.retrieve_map_direct(
                    self.uri, bbox, srs, size, image_format, styles, layers)
            except Exception as e:
                logger.info('Failed to use retrieve_map_direct, %s' % e)

        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(image.read())
        img_temp.flush()

        image_filename = self.slug + '.' + image_format.split('/')[1]

        self.preview.save(image_filename, File(img_temp), save=False)

        if not imghdr.what(self.preview.path):
            logger.info('The image is not valid')
            self.preview = ''

    @staticmethod
    def construct_url(uri, bbox, srs, size, image_format, styles, layers):
        """Constructing URL for retrieving image from WMS Server."""
        full_uri = uri
        full_uri += '&BBOX=%s' % ",".join(map(str, bbox))
        full_uri += '&SRS=%s' % srs
        full_uri += '&HEIGHT=%d&WIDTH=%d' % size
        full_uri += '&TRANSPARENT=true'
        full_uri += '&FORMAT=%s' % image_format
        full_uri += '&STYLES=%s' % ",".join(map(str, styles))
        full_uri += '&LAYERS=%s' % ','.join(layers)
        full_uri += '&VERSION=1.1.1'
        full_uri += '&REQUEST=GetMap'
        full_uri += '&SERVICE=WMS'

        return full_uri

    @staticmethod
    def retrieve_map_owslib(
            uri, bbox, srs, size, image_format, styles, layers, wms=None):
        """Retrieve image of a map from wms server using owslib."""

        if not wms:
            # Get the wms object
            wms = WebMapService(uri)

        # This is important to make sure they have the same length
        if len(styles) != len(layers):
            styles = [''] * len(layers)

        image = wms.getmap(
            layers=layers,
            styles=styles,
            srs=srs,
            bbox=bbox,
            size=size,
            format=image_format,
            transparent=True
        )

        return image

    def retrieve_map_direct(
            self, uri, bbox, srs, size, image_format, styles, layers):
        """Retrieve map image from wms server using direct get map request."""
        full_uri = self.construct_url(
            uri, bbox, srs, size, image_format, styles, layers)
        image = urllib.urlopen(full_uri)

        return image
