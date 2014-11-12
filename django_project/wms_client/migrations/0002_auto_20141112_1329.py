# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms_client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wmsresource',
            name='descriptions',
            field=models.TextField(help_text=b'This is similar to abstract part of a wms resources.', blank=True),
            preserve_default=True,
        ),
    ]
