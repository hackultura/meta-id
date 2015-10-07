from rest_framework import serializers

from .models import Ente


class TelefoneField(serializers.JSONField):

    adicionado_em = serializers.DateField()
    valido = serializers.BooleanField()
    publico = serializers.BooleanField()
    numero = serializers.IntegerField()


class EnteSerializer(serializers.ModelSerializer):

    id_pub = serializers.UUIDField(required=False)
    telefone = TelefoneField(required=False)

    class Meta:
        model = Ente
        fields = (
            'id_pub',
            'nome',
            'endereco',
            'bairro',
            'uf',
            'cep',
            'telefone'
        )
