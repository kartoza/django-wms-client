# coding=utf-8
"""Module related to test for all the models."""
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from wms_client.tests.model_factories import UserFactory


class UserMapViewTests(TestCase):
    """Class for testing user map view."""
    def setUp(self):
        """Run for each test."""
        self.email = 'test@gmail.com'
        self.password = 'test'
        self.user = UserFactory.create(
            email=self.email,
            password=self.password,
            role__name='Test User',
            is_confirmed=True)
        self.client = Client()

    def test_index(self):
        """Test for index view."""
        response = self.client.get(reverse('wms_client:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wms_client/legend.html')
        self.assertTemplateUsed(response, 'wms_client/data_privacy.html')
        self.assertContains(response, 'Sign Up')
        self.assertContains(response, 'Log In')

    def test_show_update_page(self):
        """Test showing update user page view."""
        # Login first
        self.assertTrue(
            self.client.login(email=self.email, password=self.password))

        response = self.client.get(reverse('wms_client:update_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wms_client/account/edit_user.html')

    def test_update_basic_information(self):
        """Test update basic information."""
        # Login first
        self.assertTrue(
            self.client.login(email=self.email, password=self.password))

        form_content = dict(
            {
                'name': 'UpdatedName',
                'url': 'http://localhost/cgi-bin/wms?map=foo',
                'layers': 'foo',
            }
        )
        response = self.client.post(
            reverse('wms_client:update'), form_content)
        self.assertRedirects(
            response,
            reverse('wms_client:update') + '#basic-information',
            302,
            200)
        wms = UserFactory(name=self.name)
        self.assertEqual(wms.name, form_content['name'])


