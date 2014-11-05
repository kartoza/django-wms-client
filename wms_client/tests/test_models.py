# coding=utf-8
"""Module related to test for all the models."""
from django.test import TestCase

from wms_client.tests.model_factories import WMSFactory


class TestRole(TestCase):
    """Class to test Role model."""
    def setUp(self):
        pass

    def test_create_wms(self):
        """Method to test wms creation."""
        wms = RoleFactory.create()
        message = 'The wms is not instantiated successfully.'
        self.assertIsNotNone(wms.id, message)

    def test_read_wms(self):
        """Method to test reading wms."""
        wms_name = 'Testing Role'
        wms = RoleFactory.create(name=wms_name)
        message = 'The wms name should be %s, but it gives %s' % (
            wms_name, wms.name)
        self.assertEqual(wms_name, wms.name, message)

    def test_update_wms(self):
        """Method to test updating wms."""
        wms = RoleFactory.create(name='Testing User')
        wms_name = 'Updated Testing User'
        wms.name = wms_name
        wms.save()
        message = 'The wms name should be %s, but it gives %s' % (
            wms_name, wms.name)
        self.assertEqual(wms_name, wms.name, message)

    def test_delete_wms(self):
        """Method to test deleting wms."""
        wms = RoleFactory.create()
        self.assertIsNotNone(wms.id)
        wms.delete()
        message = 'The wms is not deleted.'
        self.assertIsNone(wms.id, message)
