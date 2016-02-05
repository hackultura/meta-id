# -*- coding: utf-8 -*-

import json
import datetime

from mock import patch
from django.core.urlresolvers import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase


class AnaliseEnteTest(APITestCase):

    def setUp(self):

        self.maxDiff = None
        self.date_now = datetime.datetime(2015, 12, 8)

        self.nome = {
            "slug": "cicrano-beltrano",
            "nome": "Cicrano Beltrano"
        }

        self.user_slug = self.nome['slug']
        self.user_url = reverse(
            'api:analises:list-ente',
            kwargs={'slug': self.user_slug}
        )
        self.ente_url = reverse(
            'api:entes'
        )

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

        data = {}
        data.update(self.nome)
        data.update(self.dados_pessoais)
        data.update({"classificacoes": self.classificacoes})

        self.user = self.client.post(self.ente_url, data, format='json')
        self.assertEqual(self.user.status_code, status.HTTP_201_CREATED)

    def test_access_url_to_analises(self):

        response = self.client.get(self.user_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_return_all_analises_from_an_ente(self):

        data = json.loads(self.user.content.decode('utf-8'))
        user_slug = self.nome["slug"]
        user_id_pub = data["id_pub"]

        url_analise_ente = reverse(
            'api:analises:list-ente',
            kwargs={'slug': user_slug}
        )
        response = self.client.get(url_analise_ente)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
