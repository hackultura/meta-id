# -*- coding: utf-8 -*-

import os

from django.test import TestCase
from django.db import models
from django.conf import settings

from model_mommy import mommy

from meta_id.test.fixtures import file
from meta_id.core.models import (
    PortfolioArquivo,
    PortfolioImagem,
    Ente,
    PerfilArtistico
)


class PortfolioArquivoTest(TestCase):
    def test_should_field_nome(self):
        field = PortfolioArquivo._meta.get_field('nome')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_criado_em(self):
        field = PortfolioArquivo._meta.get_field('criado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_atualizado_em(self):
        field = PortfolioArquivo._meta.get_field('atualizado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_arquivo(self):
        field = PortfolioArquivo._meta.get_field('arquivo')
        self.assertIsInstance(field, models.FileField)


class PortfolioImagemTest(TestCase):
    def test_should_field_nome(self):
        field = PortfolioImagem._meta.get_field('nome')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_criado_em(self):
        field = PortfolioImagem._meta.get_field('criado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_atualizado_em(self):
        field = PortfolioImagem._meta.get_field('atualizado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_imagem(self):
        field = PortfolioImagem._meta.get_field('imagem')
        self.assertIsInstance(field, models.ImageField)
