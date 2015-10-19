from rest_framework import serializers

from .models import Ente, ClassificacaoArtistica
from .fields import JSONField


class EnteSerializer(serializers.ModelSerializer):

    id_pub = serializers.UUIDField(required=False)
    informacoes_geograficas = JSONField(required=False)
    telefone = JSONField(required=False)

    class Meta:
        model = Ente
        fields = (
            'id_pub',
            'nome',
            'informacoes_geograficas',
            'telefone',
        )


class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificacaoArtistica
        fields = ("area", "estilos",)
