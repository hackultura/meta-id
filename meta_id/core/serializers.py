# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Ente, ClassificacaoArtistica, PerfilArtistico
from .fields import EnderecoField, TelefoneField


class EnteSerializer(serializers.ModelSerializer):
    id_pub = serializers.UUIDField(required=False)
    informacoes_geograficas = EnderecoField(required=False)
    telefone = TelefoneField(required=False)
    nascimento = serializers.DateField()
    classificacoes = serializers.JSONField()

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
