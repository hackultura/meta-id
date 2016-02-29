# -*- coding: utf-8 -*-

from rest_framework import serializers

from meta_id.core.models import Ente


class AnaliseEnteSerializer(serializers.Serializer):
    analise = serializers.JSONField()

    class Meta:
        model = Ente
        fields = ('analise',)

