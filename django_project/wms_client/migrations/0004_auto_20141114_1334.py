# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms_client', '0003_auto_20141114_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wmsresource',
            old_name='descriptions',
            new_name='description'
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='description',
            field=models.TextField(help_text=b'Description for the map. If left blank, the WMS abstract text will be used.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='east',
            field=models.FloatField(help_text=b'Eastern boundary in decimal degrees. Will default to maxima of all layers.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='layers',
            field=models.CharField(help_text=b'The layers to be included in the map. Separate with commas, no spaces between the commas. If left blank the top of the layer list tree will be used by default.', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='max_zoom',
            field=models.IntegerField(default=19, help_text=b'Default minimum zoom level (1-19) for this map. Defaults to 19', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='min_zoom',
            field=models.IntegerField(help_text=b'Default minimum zoom level (1-19) for this map.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='name',
            field=models.CharField(help_text=b'A name for the WMS map.', unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='north',
            field=models.FloatField(help_text=b'Northern boundary in decimal degrees. Will default to maxima of all layers.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='south',
            field=models.FloatField(help_text=b'Southern boundary in decimal degrees. Will default to minima of all layers.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='west',
            field=models.FloatField(help_text=b'Western boundary in decimal degrees. Will default to minima of all layers.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='zoom',
            field=models.IntegerField(help_text=b'Default zoom level (1-19) for this map.', blank=True),
            preserve_default=True,
        ),
    ]
