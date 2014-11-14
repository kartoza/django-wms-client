# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wms_client', '0004_auto_20141114_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wmsresource',
            name='east',
            field=models.FloatField(help_text=b'Eastern boundary in decimal degrees. Will default to maxima of all layers.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='max_zoom',
            field=models.IntegerField(default=19, help_text=b'Default minimum zoom level (0-19) for this map. Defaults to 19', blank=True, validators=[django.core.validators.MaxValueValidator(19), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='min_zoom',
            field=models.IntegerField(help_text=b'Default minimum zoom level (0-19) for this map.', blank=True, validators=[django.core.validators.MaxValueValidator(19), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='north',
            field=models.FloatField(help_text=b'Northern boundary in decimal degrees. Will default to maxima of all layers.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='south',
            field=models.FloatField(help_text=b'Southern boundary in decimal degrees. Will default to minima of all layers.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='west',
            field=models.FloatField(help_text=b'Western boundary in decimal degrees. Will default to minima of all layers.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='zoom',
            field=models.IntegerField(help_text=b'Default zoom level (1-19) for this map.', blank=True, validators=[django.core.validators.MaxValueValidator(19), django.core.validators.MinValueValidator(0)]),
            preserve_default=True,
        ),
    ]
