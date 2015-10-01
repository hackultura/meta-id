from rest_framework import serializers

from .models import Ente


class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ente
        fields = ('endereco', 'bairro', 'uf', 'cep')


class EnteSerializer(serializers.ModelSerializer):

    id_pub = serializers.UUIDField(required=False)
    nome = serializers.CharField(max_length=100)
    informacoes_geograficas = EnderecoSerializer()

    class Meta:
        model = Ente
        fields = ('id_pub', 'nome', 'informacoes_geograficas')

    def create(self, validated_data):
        return Ente.objects.create(
            nome=validated_data['nome'],
            endereco=validated_data['informacoes_geograficas']['endereco'],
            bairro=validated_data['informacoes_geograficas']['bairro'],
            uf=validated_data['informacoes_geograficas']['uf'],
            cep=validated_data['informacoes_geograficas']['cep'],
        )
