# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WMSResource',
            fields=[
                ('slug', models.SlugField(unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(help_text=b'The identifier for the WMS Resource.', unique=True, max_length=100)),
                ('uri', models.CharField(help_text=b'URI for the WMS resource', max_length=100)),
                ('layers', models.CharField(help_text=b'The layers that you want to retrieve.', max_length=100, blank=True)),
                ('descriptions', models.TextField(help_text=b'This is similar to abstract part of a wms resources.')),
                ('preview', models.ImageField(help_text=b'Preview image for this WMS Resource.', upload_to=b'wms_preview', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
