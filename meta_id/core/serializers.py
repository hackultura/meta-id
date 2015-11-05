# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_localflavor.br.serializers import BRCPFField

from .models import Ente, ClassificacaoArtistica, PerfilArtistico
from .fields import EnderecoField, TelefoneField, ClassificacoesField


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
