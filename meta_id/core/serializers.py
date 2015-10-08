from rest_framework import serializers

from .models import Ente


class EnderecoField(serializers.JSONField):

    endereco = serializers.CharField()
    bairro = serializers.CharField()
    uf = serializers.CharField()
    cep = serializers.CharField()


class TelefoneField(serializers.JSONField):

    adicionado_em = serializers.DateField()
    valido = serializers.BooleanField()
    publico = serializers.BooleanField()
    numero = serializers.IntegerField()


class AtuacaoField(serializers.JSONField):

    atuacao = serializers.CharField()
    area = serializers.CharField()
    estilo = serializers.CharField()
    experiencia = serializers.CharField()


class EnteSerializer(serializers.ModelSerializer):

    id_pub = serializers.UUIDField(required=False)
    informacoes_geograficas = EnderecoField(required=False)
    telefone = TelefoneField(required=False)
    atuacao = AtuacaoField(required=False)

    class Meta:
        model = Ente
        fields = (
            'id_pub',
            'nome',
            'informacoes_geograficas',
            'telefone',
            'atuacao'
        )
