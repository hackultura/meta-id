# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Ente, ClassificacaoArtistica, PerfilArtistico
from .fields import EnderecoField, TelefoneField


class EnteSerializer(serializers.ModelSerializer):

    id_pub = serializers.UUIDField(required=False)
    informacoes_geograficas = EnderecoField(required=False)
    telefone = TelefoneField(required=False)
    nascimento = serializers.DateField()
    class Meta:
        model = Ente
        fields = (
            'id_pub',
            'slug',
            'nome',
            'informacoes_geograficas',
            'telefone',
            'email',
            'nascimento',
        )
        read_only_fields = ('slug')


class PerfilArtisticoSerializer(serializers.ModelSerializer):
    id_pub = serializers.UUIDField(required=False)
    tipo_atuacao = serializers.SerializerMethodField()
    atuacao = serializers.ChoiceField(
        choices=PerfilArtistico.ATUACAO_CHOICES,
        write_only=True
    )
    tempo_experiencia = serializers.SerializerMethodField()
    classificacao = serializers.JSONField()
    class Meta:
        model = PerfilArtistico
        fields = (
            "id_pub",
            "slug",
            "nome",
            "atuacao",
            "tipo_atuacao",
            "classificacao",
            "experiencia",
            "tempo_experiencia",
            "historico",
        )
        read_only_fields = ("id_pub", "slug", "tipo_atuacao",
                            "tempo_experiencia",)
        extra_kwargs = {
            'experiencia': {'write_only': True}
        }

    def get_tipo_atuacao(self, obj):
        return obj.get_atuacao_display()

    def get_tempo_experiencia(self, obj):
            if obj.experiencia > 1:
                return "{0} Anos".format(obj.experiencia)
            else:
                return "{0} Ano".format(obj.experiencia)


class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificacaoArtistica
        fields = ("area", "estilos",)
