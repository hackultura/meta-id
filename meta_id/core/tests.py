from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from model_mommy import mommy

from .models import Ente


class EnteTest(APITestCase):

    def setUp(self):

        self.url = reverse('api:entes-list')
        self.data = {
            "nome": "Cicrano Beltrano",
            "endereco": "Av. Vladmir Herzog, 156",
            "bairro": "Jardim Botanico",
            "uf": "DF",
            "cep": "71000-000",
        }

    def test_access_url_to_list_all_entes(self):

        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_persist_an_ente(self):

        self.ente = mommy.make(Ente, nome="Fulano Cicrano")

        entes = Ente.objects.first()

        self.assertEqual(entes.nome, 'Fulano Cicrano')
        self.assertEqual(Ente.objects.count(), 1)

    def test_persist_an_ente_using_POST(self):

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ente.objects.first().nome, 'Cicrano Beltrano')

    def test_persist_an_ente_returning_uuid_as_id_pub(self):

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertContains(response, 'id_pub', status_code=201)

    def test_persist_geographic_informantion_of_ente(self):

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.content)
        ente = Ente.objects.first()
        self.assertEqual(ente.uf, 'DF')
        self.assertContains(self.data, response, status_code=201)
