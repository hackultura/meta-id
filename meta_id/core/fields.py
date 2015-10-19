# -*- coding: utf-8 -*-

import re

from django.utils import timezone
from rest_framework import serializers


class EnderecoField(serializers.JSONField):
    def to_internal_value(self, data):
        validated_data = []

        for item in data:
            if item.get('endereco') in [None, ""]:
                msg = u"Insira todo o endereço corretamente."
                raise serializers.ValidationError(msg)
            if item.get('uf') in [None, ""]:
                msg = u"Insira a unidade federativa."
                raise serializers.ValidationError(msg)
            if item.get('cep') is None:
                msg = u"Não foi encontrado o cep."
                raise serializers.ValidationError(msg)
            if re.search(r"\d{5}-\d{3}", item.get('cep')) is None:
                msg = u"Digite um CEP válido."
                raise serializers.ValidationError(msg)
            if item.get('bairro') in [None, ""]:
                msg = u"Não foi encontrado o bairro."
                raise serializers.ValidationError(msg)

            item["adicionado_em"] = timezone.now()
            validated_data.append(item)

        return validated_data


class TelefoneField(serializers.JSONField):
    def to_internal_value(self, data):
        validated_data = []

        for item in data:
            item["valido"] = True
            item["adicionado_em"] = timezone.now()
            validated_data.append(item)

        return validated_data
