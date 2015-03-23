# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wms_client', '0005_auto_20141114_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wmsresource',
            name='max_zoom',
            field=models.IntegerField(default=19, help_text=b'Default minimum zoom level (0-19) for this map. Defaults to 19', null=True, blank=True, validators=[django.core.validators.MaxValueValidator(19), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='wmsresource',
            name='min_zoom',
            field=models.IntegerField(blank=True, help_text=b'Default minimum zoom level (0-19) for this map.', null=True, validators=[django.core.validators.MaxValueValidator(19), django.core.validators.MinValueValidator(0)]),
        ),
    ]
