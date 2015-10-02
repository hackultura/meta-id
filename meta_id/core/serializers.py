from rest_framework import serializers

from .models import Ente


class EnteSerializer(serializers.ModelSerializer):

    id_pub = serializers.UUIDField(required=False)

    class Meta:
        model = Ente
        fields = ('id_pub', 'nome', 'endereco', 'bairro', 'uf', 'cep')
