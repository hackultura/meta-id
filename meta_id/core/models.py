# -*- coding: utf-8 -*-
import uuid
import os
import re
import shutil

from django.db import models
from django.conf import settings
from django.http import Http404
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save, pre_delete
from django.dispatch.dispatcher import receiver
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from postgres.fields import JSONField
from model_utils import Choices

from meta_id.core.signals import (
    remove_portfolio_file,
    remove_portfolio_folder,
)


def generate_portfolio_filepath(instance, filename):
    """
    Método callable usado para preparar um caminho para
    os arquivos dos portfólios dos perfis artísticos.

    :param instance:
        Instancia do registro do modelo
    :param filename:
        Nome do arquivo que acabou de fazer upload
    """
    cpf = re.sub(r'\W', '_', instance.perfil.ente.cpf)
    path = "portfolios/{ente}/{profile_uid}/{type}/{filename}".format(
        ente=cpf,
        profile_uid=instance.perfil.id_pub,
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


def get_portfolio_or_404(type=None, uid=None):
    """
    Retorna o portfolio selecionado pelo seu uid, caso contrario
    retorna o objeto Http404.

    :param type:
        Define o tipo do conteudo (file, image, album, audio, video)
    :param uid:
        UID do portfolio
    """
    try:
        if type == "file":
            return PortfolioArquivo.objects.get(id_pub=uid)
        if type == "image":
            return PortfolioImagem.objects.get(id_pub=uid)
        if type == "audio":
            return PortfolioAudio.objects.get(id_pub=uid)
        if type == "video":
            return PortfolioVideo.objects.get(id_pub=uid)
        else:
            raise ValueError("Tipo de conteúdo inválido para pesquisa.")
    except ObjectDoesNotExist:
        raise Http404()


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
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    informacoes_geograficas = JSONField(blank=True, null=True)
    telefone = JSONField(blank=True, null=True)
    cpf = models.CharField(_(u"CPF"), max_length=15, blank=False)
    nascimento = models.DateField()
    classificacoes = JSONField()
    documentos = JSONField(blank=True)

    class Meta:
        verbose_name = "ente"
        verbose_name_plural = "entes"

    def __str__(self):
        return self.user.name

    def get_absolute_url(self):
        return reverse('core.views.entes', args=[str(self.id)])


class PerfilArtistico(models.Model):
    id_pub = models.UUIDField(default=uuid.uuid4, editable=False)
    ente = models.ForeignKey('Ente', related_name="perfis")
    nome = models.CharField(_(u"Nome Artístico"), max_length=60)
    slug = AutoSlugField(populate_from='nome', overwrite=True)
    historico = models.CharField(_(u"Breve Histórico"), max_length=255)

    def delete(self, *args, **kwargs):
        remove_portfolio_folder.send(sender=self.__class__, instance=self)
        super(PerfilArtistico, self).delete(*args, **kwargs)


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

    def delete(self, *args, **kwargs):
        remove_portfolio_file.send(sender=self.__class__, instance=self)
        super(Conteudo, self).delete(*args, **kwargs)


class ConteudoImagemMixin(models.Model):
    """
    Modelo abstrato que trata das imagens usadas nas
    entidades do sistema.
    """
    imagem = models.ImageField(upload_to=generate_portfolio_filepath)

    class Meta:
        abstract = True


class PortfolioArquivo(Conteudo):
    perfil = models.ForeignKey('PerfilArtistico', related_name='arquivos')
    nome = models.CharField(max_length=255, blank=False)
    arquivo = models.FileField(upload_to=generate_portfolio_filepath)

    @property
    def _type(self):
        """Define o tipo de conteudo"""
        return "file"


class PortfolioImagem(ConteudoImagemMixin, Conteudo):
    perfil = models.ForeignKey('PerfilArtistico', related_name='imagens')
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
    perfil = models.ForeignKey('PerfilArtistico', related_name='audios')
    nome = models.CharField(max_length=255, blank=False)
    audio = models.FileField(upload_to=generate_portfolio_filepath)

    @property
    def _type(self):
        """Define o tipo de conteudo"""
        return "audio"


class PortfolioVideo(Conteudo):
    perfil = models.ForeignKey('PerfilArtistico', related_name='videos')
    nome = models.CharField(max_length=255, blank=False)
    url = models.URLField(max_length=255, blank=False)
    plataforma = models.CharField(max_length=30, blank=False)

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
    dono = models.UUIDField()
    nome = models.CharField(max_length=255, blank=False)
    vencimento = models.DateField()
    arquivo = models.FileField(upload_to="documentacao/%Y/%m/%d")

    def _get_owner(self):
        try:
            return Ente.objects.get(id_pub=self.dono)
        except Ente.DoesNotExist:
            pass
        try:
            return PerfilArtistico.objects.get(id_pub=self.dono)
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


# Signals
@receiver(remove_portfolio_file)
def delete_portfolio_file(sender, instance, **kwargs):
    if hasattr(instance, 'arquivo'):
        file = instance.arquivo
    elif hasattr(instance, 'imagem'):
        file = instance.imagem
    elif hasattr(instance, 'audio'):
        file = instance.audio

    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    if os.path.exists(file_path):
        os.remove(os.path.join(settings.MEDIA_ROOT, file.name))


@receiver(remove_portfolio_folder)
def delete_portfolio_folder(sender, instance, **kwargs):
    slug = instance.slug
    path = "portfolios/{0}".format(slug)
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, path))


def _search_document(documentos, file):
    file = file.split("/")[-1]
    filename, format = file.split(".")

    for documento in documentos:
        if documento.get("arquivo") == filename:
            return documento
    return None


@receiver(post_save, sender=Documento)
def register_content_by_ente_or_profile(sender, instance, created, **kwargs):
    """
    Captura os metadados e uid do documento inserido e salva
    no campo JSON do modelo de ente ou perfil.
    """
    owner = instance._get_owner()
    if not isinstance(owner.documentos, list):
        owner.documentos = []

    filename = instance.arquivo.name.split("/")[-1]
    filename, format = filename.split(".")
    owner.documentos.append({
        "nome": instance.nome,
        "arquivo": filename,
        "formato": format,
        "tamanho": instance.arquivo.size,
        "enviado_em": instance.criado_em,
        "vencimento": instance.vencimento
    })
    owner.save()


# TODO: Fique registrado se caso essa tarefa for custosa
# pela quantidade de documentos futuramente, considere isso
# uma tarefa para o celery.
@receiver(pre_delete, sender=Documento)
def remove_content_of_owner(sender, instance, **kwargs):
    """
    Antes da remocao do conteudo, ele e retirado do JSON
    de documentacao do ente ou perfil.
    """
    owner = instance._get_owner()
    documentos = owner.documentos
    resultado = _search_document(documentos, instance.arquivo.name)
    documentos.remove(resultado)
    owner.documentos = documentos
    owner.save()
