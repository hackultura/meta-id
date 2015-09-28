from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from model_mommy import mommy

from .models import Ente


class EnteTest(APITestCase):

    def setUp(self):

        self.url = reverse('api:entes-list')

    def test_access_url_to_list_all_entes(self):

        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_persist_an_ente(self):

        self.ente = mommy.make(Ente, nome="Fulano Cicrano")

        entes = Ente.objects.first()

        self.assertEqual(entes.nome, 'Fulano Cicrano')
        self.assertEqual(Ente.objects.count(), 1)

    def test_persist_an_ente_using_POST(self):

        data = {
            'nome': 'Cicrano Beltrano'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ente.objects.first().nome, 'Cicrano Beltrano')

    def test_persist_an_ente_returning_uuid_as_id_pub(self):

        data = {
            'nome': 'Cicrano Beltrano'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertContains(response, 'id_pub', status_code=201)
