from rest_framework import serializers

from .models import Ente


class EnteSerializer(serializers.Serializer):

    nome = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Ente.objects.create(**validated_data)