# -*- coding: utf-8 -*-

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
        pass
    if type == "video":
        pass
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
            'slug',
            'nome',
            'informacoes_geograficas',
            'telefone',
            'email',
            'cpf',
            'nascimento',
            'classificacoes',
            'perfis',
        )
        read_only_fields = ('slug')


class PerfilArtisticoSerializer(serializers.ModelSerializer):
    id_pub = serializers.UUIDField(required=False)
    class Meta:
        model = PerfilArtistico
        fields = (
            "id_pub",
            "slug",
            "nome",
            "historico",
        )
        read_only_fields = ("id_pub", "slug",)


class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificacaoArtistica
        fields = ("area", "estilos",)


class PortfolioArquivoSerializer(serializers.ModelSerializer):
    conteudo = FileBase64Field(source='arquivo')
    class Meta:
        model = PortfolioArquivo
        fields = (
            'nome',
            'conteudo',
        )


class PortfolioImageSerializer(serializers.ModelSerializer):
    conteudo = FileBase64Field(source='imagem')
    class Meta:
        model = PortfolioImagem
        fields = (
            'descricao',
            'conteudo',
        )


class PortfolioImagemAlbumSerializer(serializers.ModelSerializer):
    conteudo = FileBase64Field(source='imagem')
    class Meta:
        model = PortfolioImagemAlbum
        fields = (
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

    def create(self, validated_data):
        import ipdb; ipdb.set_trace()
        return super(PortfolioAlbumSerializer, self).create(validated_data)
