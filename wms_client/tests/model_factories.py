# coding=utf-8
"""Model factory definitions for models."""

import factory
from factory import DjangoModelFactory

from wms_client.models import WMS


class WMSFactory(DjangoModelFactory):
    """Factory class for WMS model."""
    class Meta:
        """Meta definition."""
        model = WMS

    name = factory.Sequence(lambda n: 'WMS %s' % n)
    sort_number = 1
