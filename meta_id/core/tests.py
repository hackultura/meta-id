from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from model_mommy import mommy

from .models import Ente


class EnteTest(APITestCase):

    def setUp(self):

        self.maxDiff = None

        self.url = reverse('api:entes-list')
        self.nome = {
            "nome": "Cicrano Beltrano"
        }
        self.endereco = {
            "informacoes_geograficas": [
                {
                    "endereco": "Av. Vladmir Herzog, 156",
                    "bairro": "Jardim Botanico",
                    "uf": "DF",
                    "cep": "71000-000",
                    "adicionado_em": "01/01/2015",
                    "comprovacao": {
                        "UUID": "",
                        "url": "",
                    }
                }
            ]
        }

        self.telefone = {
            "telefone": [
                {
                    "comercial": "61 9111-1111",
                    "adicionado_em": "01/01/2015",
                    "valido": "True",
                },
                {
                    "residencial": "61 8111-1111",
                    "adicionado_em": "01/02/2015",
                    "valido": "True",
                },
                {
                    "comercial": "61 3111-1111",
                    "adicionado_em": "01/12/2014",
                    "valido": "False",
                },
            ]
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

        response = self.client.post(self.url, self.nome, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ente.objects.first().nome, 'Cicrano Beltrano')

    def test_persist_an_ente_returning_uuid_as_id_pub(self):

        response = self.client.post(self.url, self.nome, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertContains(response, 'id_pub', status_code=201)

    def test_persist_geographic_informantion_of_ente(self):

        data = self.nome
        data.update(self.endereco)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = dict(**response.data)
        response_data.pop('id_pub')
        response_data.pop('telefone')
        self.assertDictEqual(response_data, data)

    def test_persist_a_telephone_number_of_ente(self):

        data = self.nome
        data.update(self.endereco)
        data.update(self.telefone)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.content)
        response_data = dict(**response.data)
        response_data.pop('id_pub')
        self.assertDictEqual(response_data, data)
