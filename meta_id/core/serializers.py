from rest_framework import serializers

from .models import Ente, ClassificacaoArtistica
from .fields import EnderecoField, TelefoneField


class EnteSerializer(serializers.ModelSerializer):

    id_pub = serializers.UUIDField(required=False)
    informacoes_geograficas = EnderecoField(required=False)
    telefone = TelefoneField(required=False)

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
