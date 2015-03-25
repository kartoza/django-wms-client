# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms_client', '0006_auto_20141114_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wmsresource',
            name='layers',
            field=models.TextField(help_text=b'The layers to be included in the map. Separate with commas, no spaces between the commas. If left blank the top of the layer list tree will be used by default.', blank=True),
            preserve_default=True,
        ),
    ]
