# -*- coding: utf-8 -*-

import json
import datetime

from mock import patch
from django.core.urlresolvers import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase


class AnaliseTest(APITestCase):

    def setUp(self):

        self.maxDiff = None
        self.date_now = datetime.datetime(2015, 12, 8)
        self.url_analise = reverse('analise:analises')
        self.url_user = reverse('api:entes')

        self.nome = {
            "slug": "cicrano-beltrano",
            "nome": "Cicrano Beltrano"
        }

        with patch.object(timezone, 'now', return_value=self.date_now) as mock_now:
            self.endereco = {
                "informacoes_geograficas": [
                    {
                        "endereco": "Av. Vladmir Herzog, 156",
                        "bairro": "Jardim Botanico",
                        "cidade": "Sudoeste",
                        "uf": "DF",
                        "cep": "71000-000",
                        "adicionado_em": timezone.now()
                    }
                ]
            }

            self.telefone = {
                "telefone": [
                    {
                        "comercial": "61 9111-1111",
                        "adicionado_em": timezone.now(),
                        "valido": True,
                    },
                    {
                        "residencial": "61 8111-1111",
                        "adicionado_em": timezone.now(),
                        "valido": True,
                    },
                    {
                        "comercial": "61 3111-1111",
                        "adicionado_em": timezone.now(),
                        "valido": True,
                    },
                ]
            }

            self.dados_pessoais = {
                "email": "fulano.cicrano@mail.com",
                "cpf": "885.723.504-11",
                "nascimento": "01/07/1984"
            }

            self.classificacoes = [
                {
                    "atuacao": "Produção",
                    "area": "Ópera",
                    "estilo": "Canto",
                    "experiencia": 1
                },
                {
                    "atuacao": "Produção",
                    "area": "Artes Cenicas",
                    "estilo": "Exposições em geral",
                    "experiencia": 3
                }
            ]

    def test_access_url_to_analises(self):

        response = self.client.get(self.url_analise, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_return_all_analises_from_an_ente(self):

        data = {}
        data.update(self.nome)
        data.update(self.dados_pessoais)
        data.update({"classificacoes": self.classificacoes})

        user = self.client.post(self.url_user, data, format='json')
        self.assertEqual(user.status_code, status.HTTP_201_CREATED)

        data = json.loads(user.content.decode('utf-8'))
        user_id_pub = data["id_pub"]

        url_analise_ente = reverse('analise:list-ente', kwargs={'id_pub': user_id_pub})
        response = self.client.get(url_analise_ente)

        self.assertEqual(response.status_code, status.status_200_OK)
