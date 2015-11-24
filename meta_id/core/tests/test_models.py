# -*- coding: utf-8 -*-

import os

from django.test import TestCase
from django.db import models
from django.conf import settings

from model_mommy import mommy

from meta_id.test.fixtures import file
from meta_id.core.models import (
    PortfolioArquivo,
    PortfolioAlbum,
    PortfolioImagem,
    PortfolioImagemAlbum,
    PortfolioAudio,
    PortfolioVideo,
    Ente,
    PerfilArtistico,
    Documento,
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
    def test_should_field_descricao(self):
        field = PortfolioImagem._meta.get_field('descricao')
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


class PortfolioImagemAlbumTest(TestCase):
    def test_should_field_album(self):
        field = PortfolioImagemAlbum._meta.get_field('album')
        self.assertIsInstance(field, models.ForeignKey)

    def test_should_field_criado_em(self):
        field = PortfolioImagemAlbum._meta.get_field('criado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_atualizado_em(self):
        field = PortfolioImagemAlbum._meta.get_field('atualizado_em')
        self.assertIsInstance(field, models.DateTimeField)


class PortfolioAlbumTest(TestCase):
    def test_should_field_nome(self):
        field = PortfolioAlbum._meta.get_field('nome')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_criado_em(self):
        field = PortfolioAlbum._meta.get_field('criado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_atualizado_em(self):
        field = PortfolioAlbum._meta.get_field('atualizado_em')
        self.assertIsInstance(field, models.DateTimeField)


class PortfolioAudioTest(TestCase):
    def test_should_field_nome(self):
        field = PortfolioAudio._meta.get_field('nome')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_criado_em(self):
        field = PortfolioAudio._meta.get_field('criado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_atualizado_em(self):
        field = PortfolioAudio._meta.get_field('atualizado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_audio(self):
        field = PortfolioAudio._meta.get_field('audio')
        self.assertIsInstance(field, models.FileField)


class PortfolioVideoTest(TestCase):
    def test_should_field_nome(self):
        field = PortfolioVideo._meta.get_field('nome')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_criado_em(self):
        field = PortfolioVideo._meta.get_field('criado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_atualizado_em(self):
        field = PortfolioVideo._meta.get_field('atualizado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_url(self):
        field = PortfolioVideo._meta.get_field('url')
        self.assertIsInstance(field, models.URLField)

    def test_should_field_plataforma(self):
        field = PortfolioVideo._meta.get_field('plataforma')
        self.assertIsInstance(field, models.CharField)


class DocumentoTest(TestCase):
    def test_should_field_nome(self):
        field = Documento._meta.get_field('nome')
        self.assertIsInstance(field, models.CharField)

    def test_should_field_vencimento(self):
        field = Documento._meta.get_field('vencimento')
        self.assertIsInstance(field, models.DateField)

    def test_should_field_criado_em(self):
        field = Documento._meta.get_field('criado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_atualizado_em(self):
        field = Documento._meta.get_field('atualizado_em')
        self.assertIsInstance(field, models.DateTimeField)

    def test_should_field_arquivo(self):
        field = Documento._meta.get_field('arquivo')
        self.assertIsInstance(field, models.FileField)
