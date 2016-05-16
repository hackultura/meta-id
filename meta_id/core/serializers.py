# -*- coding: utf-8 -*-

import re
import bitmath

from django.conf import settings
from rest_framework import serializers
from rest_localflavor.br.serializers import BRCPFField

from .models import (
    Ente,
    ClassificacaoArtistica,
    PerfilArtistico,
    PortfolioArquivo,
    PortfolioImagem,
    PortfolioImagemAlbum,
    PortfolioAlbum,
    PortfolioAudio,
    PortfolioVideo,
    Documento,
)
from .fields import (
    EnderecoField,
    TelefoneField,
    ClassificacoesField,
    FileBase64Field,
)


def generate_atuacao_json():
    """
    Trata o objeto Ente.ATUACAO_CHOICES no formato
    adequado para ser usado pelo client.
    """
    choices_map = Ente.ATUACAO_CHOICES._display_map
    atuacoes = []

    for atuacao_key in choices_map.keys():
        atuacao_dict = {}
        atuacao_dict["rotulo"] = choices_map.get(atuacao_key)
        atuacao_dict["valor"] = atuacao_key
        atuacoes.append(atuacao_dict)

    return atuacoes


def create_serializer_portfolio_type(type, **kwargs):
    """
    Cria uma instancia de um serializer de portfolios,
    baseado no tipo de conteudo passado no parametro type.

    :param type:
        Define o tipo do conteudo (file, image, album, audio, video)
    :param kwargs:
        Outros parametros enviados para o serializer selecionado
    """
    # TODO: Buscar uma melhor solução, do que esses ifs
    if type == "file":
        return PortfolioArquivoSerializer(**kwargs)
    if type == "image":
        return PortfolioImageSerializer(**kwargs)
    if type == "album":
        return PortfolioAlbumSerializer(**kwargs)
    if type == "audio":
        return PortfolioAudioSerializer(**kwargs)
    if type == "video":
        return PortfolioVideoSerializer(**kwargs)
    else:
        raise ValueError("Tipo de conteúdo do serializer inválido")


class ArquivoUploadSerializer(serializers.Serializer):
    tamanho = serializers.IntegerField(min_value=1, required=True)
    nome_arquivo = serializers.CharField(required=True)
    formato = serializers.CharField(required=True)
    base64 = FileBase64Field(source='arquivo')


class EnteSerializer(serializers.ModelSerializer):
    id_pub = serializers.UUIDField(required=False)
    informacoes_geograficas = EnderecoField(required=False)
    telefone = TelefoneField(required=False)
    nascimento = serializers.DateField()
    cpf = BRCPFField()
    classificacoes = ClassificacoesField()
    perfis = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='api:perfis-detail',
        lookup_field='slug',
        lookup_url_kwarg='slug'
    )

    class Meta:
        model = Ente
        fields = (
            'id_pub',
            'informacoes_geograficas',
            'telefone',
            'cpf',
            'nascimento',
            'classificacoes',
            'perfis',
        )
        read_only_fields = ('slug')


class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificacaoArtistica
        fields = ("area", "estilos",)


class ConteudoMixin(object):
    arquivo = serializers.FileField(max_length=255, write_only=True)
    arquivo = serializers.SerializerMethodField()
    filename = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()

    class Meta:
        fields = (
            "arquivo",
            "filename",
            "size",
        )
        read_only_fields = ("arquivo", "filename", "size",)

    def _validate_file(self, file):
        if file in [None, '']:
            raise serializers.ValidationError(
                "Ocorreu um erro no upload. Tente novamente")
        elif file.content_type not in settings.ALLOWED_FILES:
            raise serializers.ValidationError(
                "Formato de arquivo inválido para o projeto.")
        return True

    def get_arquivo(self, obj):
        """
        Trata a URL do documento
        """
        request = self.context.get('request')
        is_secure = request._request.is_secure()
        host = request._request.get_host()
        if is_secure:
            return "https://{url}{path}".format(url=host, path=obj.arquivo.url)
        else:
            return "http://{url}{path}".format(url=host, path=obj.arquivo.url)

    def get_filename(self, obj):
        filename = obj.arquivo.name.split('/')[-1]
        return re.sub('\_', ' ', filename)

    def get_size(self, obj):
        return bitmath.Byte(obj.arquivo.size).best_prefix().format(
            "{value:.2f} {unit}")


class PortfolioArquivoSerializer(ConteudoMixin, serializers.ModelSerializer):
    class Meta(ConteudoMixin.Meta):
        model = PortfolioArquivo
        fields = (
            'perfil',
            'nome',
            'arquivo',
        )
        extra_kwargs = {'perfil': {'write_only': True}}


class PortfolioImageSerializer(ConteudoMixin, serializers.ModelSerializer):
    arquivo = serializers.FileField(source="imagem")

    class Meta(ConteudoMixin.Meta):
        model = PortfolioImagem
        fields = (
            'perfil',
            'descricao',
            'arquivo',
        )
        extra_kwargs = {'perfil': {'write_only': True}}


class PortfolioImagemAlbumSerializer(serializers.ModelSerializer):
    conteudo = FileBase64Field(source='imagem')

    class Meta:
        model = PortfolioImagemAlbum
        fields = (
            'perfil',
            'conteudo',
        )


class PortfolioAlbumSerializer(serializers.ModelSerializer):
    fotos = FileBase64Field(many=True)

    class Meta:
        model = PortfolioAlbum
        fields = (
            'nome',
            'fotos',
        )


class PortfolioAudioSerializer(ConteudoMixin, serializers.ModelSerializer):
    class Meta:
        model = PortfolioAudio
        fields = (
            'perfil',
            'nome',
            'audio',
        )
        extra_kwargs = {'perfil': {'write_only': True}}


class PortfolioVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioVideo
        fields = (
            'perfil',
            'nome',
            'url',
            'plataforma',
        )
        extra_kwargs = {'perfil': {'write_only': True}}


class DocumentoSerializer(serializers.ModelSerializer):
    vencimento = serializers.DateField()

    class Meta:
        model = Documento
        fields = (
            'dono',
            'nome',
            'vencimento',
            'arquivo',
        )


class PerfilArtisticoSerializer(serializers.ModelSerializer):
    id_pub = serializers.UUIDField(required=False)
    arquivos = PortfolioArquivoSerializer(many=True, read_only=True)
    imagens = PortfolioImageSerializer(many=True, read_only=True)
    audios = PortfolioAudioSerializer(many=True, read_only=True)
    videos = PortfolioVideoSerializer(many=True, read_only=True)

    class Meta:
        model = PerfilArtistico
        fields = (
            "id_pub",
            "slug",
            "nome",
            "historico",
            "arquivos",
            "imagens",
            "audios",
            "videos",
        )
        read_only_fields = ("id_pub", "slug",)
