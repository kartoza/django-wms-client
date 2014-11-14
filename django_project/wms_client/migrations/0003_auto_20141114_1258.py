# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms_client', '0002_auto_20141112_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='wmsresource',
            name='east',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wmsresource',
            name='max_zoom',
            field=models.IntegerField(default=19),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wmsresource',
            name='min_zoom',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wmsresource',
            name='north',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wmsresource',
            name='south',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wmsresource',
            name='west',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wmsresource',
            name='zoom',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
