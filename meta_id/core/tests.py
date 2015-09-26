from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class EnteTest(APITestCase):

    def test_access_url_to_list_all_entes(self):

        url = reverse('api:entes-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
