# -*- coding: utf-8 -*-
import uuid
import os

from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from postgres.fields import JSONField
from model_utils import Choices


def generate_portfolio_filepath(instance, filename):
    """
    Método callable usado para preparar um caminho para
    os arquivos dos portfólios dos perfis artísticos.

    :param instance:
        Instancia do registro do modelo
    :param filename:
        Nome do arquivo que acabou de fazer upload
    """
    path = "portfolios/{type}/{filename}".format(
        type=instance._type,
        filename=filename
    )
    return path


def define_entity_document(entity, slug):
    """
        Faz busca de um ente ou perfil, para ser usado no
        cadastro de documentos artisticos e do ente.
    """
    if entity == "ente":
        return Ente.objects.get(slug=slug)
    if entity == "perfil":
        return PerfilArtistico.objects.get(slug=slug)
    else:
        raise ValueError("Entidade incorreta para a busca.")


class Ente(models.Model):

    ATUACAO_CHOICES = Choices(
        ("gestao", u"Gestão"),
        ("pesquisa", u"Pesquisa"),
        ("facilitacao_formacao", u"Facilitação/Formação"),
        ("producao", u"Produção"),
        ("criacao_desenv", u"Criação/Desenvolvimento Artístico"),
        ("suporte", u"Suporte Técnico"),
    )

    id_pub = models.UUIDField(default=uuid.uuid4, editable=False)
    nome = models.CharField(_('Nome'), max_length=100, blank=False)
    slug = AutoSlugField(populate_from='nome', overwrite=True)
    informacoes_geograficas = JSONField(blank=True, null=True)
    telefone = JSONField(blank=True, null=True)
    email = models.EmailField(_(u"E-mail"), blank=False)
    cpf = models.CharField(_(u"CPF"), max_length=15, blank=False)
    nascimento = models.DateField()
    classificacoes = JSONField()
    documentos = JSONField(blank=True)


    class Meta:
        verbose_name = "ente"
        verbose_name_plural = "entes"

    def __str__(self):
        return self.nome

    def get_absolute_url():
        return reverse('core.views.entes', args=[str(self.id)])


class PerfilArtistico(models.Model):
    id_pub = models.UUIDField(default=uuid.uuid4, editable=False)
    ente = models.ForeignKey('Ente', related_name="perfis")
    nome = models.CharField(_(u"Nome Artístico"), max_length=60)
    slug = AutoSlugField(populate_from='nome', overwrite=True)
    historico = models.CharField(_(u"Breve Histórico"), max_length=255)
    # TODO: Implementar campo documentos
    # documentos = JSONField()


class Conteudo(models.Model):
    """
    Modelo abstrato que traz em comum todo tipo de conteudo
    anexado nas entidades do sistema.
    """
    id_pub = models.UUIDField(default=uuid.uuid4, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ConteudoImagemMixin(models.Model):
    """
    Modelo abstrato que trata das imagens usadas nas
    entidades do sistema.
    """
    imagem = models.ImageField(upload_to=generate_portfolio_filepath)

    class Meta:
        abstract = True


class PortfolioArquivo(Conteudo):
    nome = models.CharField(max_length=255, blank=False)
    arquivo = models.FileField(upload_to=generate_portfolio_filepath)

    @property
    def _type(self):
        """Define o tipo de conteudo"""
        return "file"


class PortfolioImagem(ConteudoImagemMixin, Conteudo):
    descricao = models.CharField(max_length=255, blank=False)

    @property
    def _type(self):
        """Define o tipo de conteudo"""
        return "image"


class PortfolioImagemAlbum(ConteudoImagemMixin, Conteudo):
    album = models.ForeignKey('PortfolioAlbum', related_name='fotos')

    @property
    def _type(self):
        """Define o tipo de conteudo"""
        return "album_image"


class PortfolioAlbum(Conteudo):
    nome = models.CharField(max_length=255, blank=False)


class PortfolioAudio(Conteudo):
    nome = models.CharField(max_length=255, blank=False)
    audio = models.FileField(upload_to=generate_portfolio_filepath)

    @property
    def _type(self):
        """Define o tipo de conteudo"""
        return "audio"


class PortfolioVideo(Conteudo):
    PLATFORM_CHOICES = Choices(
        ("youtube", u"Youtube"),
        ("vimeo", u"Vimeo"),
    )
    nome = models.CharField(max_length=255, blank=False)
    url = models.URLField(max_length=255, blank=False)
    plataforma = models.CharField(max_length=30, choices=PLATFORM_CHOICES,
                                  blank=False)

    @property
    def _type(self):
        """Define o tipo de conteudo"""
        return "video"


class ClassificacaoArtistica(models.Model):
    area = models.CharField("Area Artistica", max_length=100)
    estilos = ArrayField(
        models.CharField(max_length=255)
    )


class Documento(Conteudo):
    nome = models.CharField(max_length=255, blank=False)
    vencimento = models.DateField()
    arquivo = models.FileField(upload_to="documentacao/%Y/%m/%d")

    @property
    def owner(self):
        if hasattr(self, '_owner_instance'):
            return self._owner_instance
        return None

    @owner.setter
    def owner(self, value):
        """
        Recebe o uid do owner para ser associado, seja
        um ente ou perfil
        """
        try:
            self._owner_instance = Ente.objects.get(id_pub=value)
            return
        except Ente.DoesNotExist:
            pass
        try:
           self._owner_instance = PerfilArtistico.objects.get(id_pub=value)
           return
        except PerfilArtistico.DoesNotExist:
            raise ObjectDoesNotExist("Documento nao possui um owner.")


class Registro(models.Model):
    num_ceac = models.AutoField(
        _('Numero de Registro de CEAC'),
        primary_key=True
    )
    ente = models.ForeignKey(Ente)

    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "registros"

    def __str__(self):
        return self.num_ceac

    def get_absolute_url():
        return reverse('core.views.registros')


from .signals import register_content_by_ente_or_profile
