# -*- coding: utf-8 -*-

import datetime
import json
from mock import patch
from django.core.urlresolvers import reverse
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APITestCase

from model_mommy import mommy

from .models import Ente, ClassificacaoArtistica, PerfilArtistico


class EnteTest(APITestCase):

    def setUp(self):

        self.maxDiff = None
        self.date_now = datetime.datetime(2015, 10, 19, 17, 16)

        self.url = reverse('api:entes')
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

    def test_access_url_to_list_all_entes(self):

        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_persist_an_ente(self):

        self.ente = mommy.make(Ente, nome="Fulano Cicrano",
                               classificacoes=self.classificacoes)

        entes = Ente.objects.first()

        self.assertEqual(entes.nome, 'Fulano Cicrano')
        self.assertEqual(Ente.objects.count(), 1)

    def test_persist_an_ente_using_POST(self):

        data = {}
        data.update(self.nome)
        data.update(self.dados_pessoais)
        data.update({"classificacoes": self.classificacoes})
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ente.objects.first().nome, 'Cicrano Beltrano')

    def test_update_an_ente_using_PUT(self):
        from datetime import datetime
        nascimento_date = datetime.strptime(
            self.dados_pessoais.get("nascimento"),
            "%d/%m/%Y"
        )
        ente = mommy.make(
            Ente, nome="Fulano Cicrano",
            informacoes_geograficas=self.endereco,
            telefone=self.telefone,
            email=self.dados_pessoais.get("email"),
            nascimento=nascimento_date,
            cpf="251.716.861-06",
            classificacoes=self.classificacoes
        )

        url = reverse('api:entes-detail', kwargs={'slug': ente.slug})
        response = self.client.get(self.url)
        data = json.loads(response.content.decode('utf-8'))[0]
        data["nome"] = "Nome Alterado"

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_persist_an_ente_returning_uuid_as_id_pub(self):

        data = {}
        data.update(self.nome)
        data.update(self.dados_pessoais)
        data.update({"classificacoes": self.classificacoes})
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertContains(response, 'id_pub', status_code=201)

    def test_persist_geographic_informantion_of_ente(self):

        with patch.object(timezone, 'now', return_value=self.date_now) as mock_now:
            data = self.nome
            data.update(self.endereco)
            data.update(self.dados_pessoais)
            data.update({"classificacoes": self.classificacoes})
            data.update({"perfis": []})
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            response_data = dict(**response.data)
            response_data.pop('id_pub')
            response_data.pop('telefone')
            self.assertDictEqual(response_data, data)

    def test_persist_a_telephone_number_of_ente(self):
        with patch.object(timezone, 'now', return_value=self.date_now) as mock_now:
            data = self.nome
            data.update(self.telefone)
            data.update(self.dados_pessoais)
            data.update({"classificacoes": self.classificacoes})
            data.update({"perfis": []})
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            response_data = dict(**response.data)
            response_data.pop('id_pub')
            response_data.pop('informacoes_geograficas')
            self.assertDictEqual(response_data, data)

    def test_should_retrieve_a_ente(self):
        ente = mommy.make(Ente, nome="Fulano Cicrano",
                          classificacoes=self.classificacoes)
        url = reverse('api:entes-detail', kwargs={'slug': ente.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ClassificacoesTest(APITestCase):
    def setUp(self):
        self.url = reverse('api:classificacoes-list')

        ClassificacaoArtistica.objects.create(
            area="Artes Visuais",
            estilos=["Exposicao de artes em geral"]
        )

    def test_should_get_areas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Como content retorna em bytes e o data em OrderedDict, foi
        # necessario efetuar esse decode
        # Isso foi alterado na versão 3.x do Django Rest Framework
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_data, [
            {
                "area": "Artes Visuais",
                "estilos": ["Exposicao de artes em geral"]
            }
        ])


class PerfilArtisticoTest(APITestCase):
    def setUp(self):
        classificacoes = [
            {
                "area": "Artes Visuais",
                "estilo": "Exposicoes em geral",
                "experiencia": 3
            }
        ]
        self.ente = mommy.make(Ente, nome="Fulano Cicrano",
                               classificacoes=classificacoes)
        self.perfil = PerfilArtistico.objects.create(
            nome="Cantor Fulano",
            ente=self.ente,
            historico="Breve Historico"
        )
        self.url = reverse('api:perfis', kwargs={'slug': self.ente.slug})


    def test_should_get_profiles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Como content retorna em bytes e o data em OrderedDict, foi
        # necessario efetuar esse decode
        # Isso foi alterado na versão 3.x do Django Rest Framework
        response_data = json.loads(response.content.decode('utf-8'))
        response_data[0].pop("id_pub")
        self.assertEqual(response_data, [
            {
                "slug": "cantor-fulano",
                "nome": "Cantor Fulano",
                "historico": "Breve Historico"
            }
        ])

    def test_should_post_profile(self):
        data = {
            "nome": "Tocador Fulano",
            "historico": "Breve Historico"
        }

        output_data = {
            "slug": "tocador-fulano",
            "nome": "Tocador Fulano",
            "historico": "Breve Historico"
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response.data.pop("id_pub")
        self.assertDictEqual(response.data, output_data)

    def test_should_retrieve_profile(self):
        output_data = {
            "slug": "cantor-fulano",
            "nome": "Cantor Fulano",
            "historico": "Breve Historico"
        }
        url = reverse('api:perfis-detail', kwargs={'slug': self.perfil.slug})
        response = self.client.get(url)
        response.data.pop("id_pub")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, output_data)

    def test_should_update_profile(self):
        url = reverse('api:perfis-detail', kwargs={'slug': self.perfil.slug})
        response = self.client.get(url)

        # Tratando resposta e retirando campos somente para leitura
        data = json.loads(response.content.decode('utf-8'))

        data["nome"] = "Perfil Alterado"
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
