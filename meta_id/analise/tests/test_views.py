# -*- coding: utf-8 -*-


from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class AnaliseTest(APITestCase):

    def setUp(self):

        self.maxDiff = None
        self.url = reverse('analise:analises')

        self.nome = {
            "slug": "cicrano-beltrano",
            "nome": "Cicrano Beltrano"
        }
        

    def test_access_url_to_analises(self):

        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_return_all_analises_from_an_ente(self):


