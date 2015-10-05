from rest_framework import serializers

from .models import Ente


class TelefoneSerializer(serializers.Serializer):

    adicionado_em = serializers.DateField()
    valido = serializers.BooleanField()
    publico = serializers.BooleanField()
    numero = serializers.IntegerField()

    class Meta:
        model = Telefone
        fields = ('adicionado_em', 'tipo', 'numero', 'valido')


class EnteSerializer(serializers.ModelSerializer):

    id_pub = serializers.UUIDField(required=False)

    class Meta:
        model = Ente
        fields = ('id_pub', 'nome', 'endereco', 'bairro', 'uf', 'cep')
