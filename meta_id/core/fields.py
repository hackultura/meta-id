# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

from django.utils import timezone
from rest_framework import serializers


class EnderecoField(serializers.JSONField):
    def to_internal_value(self, data):
        validated_data = []


        for item in data:
            if isinstance(item, str) or isinstance(item, unicode):
                continue
            if item.get('endereco') in [None, ""]:
                msg = u"Insira todo o endereço corretamente."
                raise serializers.ValidationError(msg)
            if item.get('cidade') in [None, ""]:
                msg = u"Insira o nome da sua cidade."
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
            if isinstance(item, str):
                continue
            item["valido"] = True
            item["adicionado_em"] = timezone.now()
            validated_data.append(item)

        return validated_data


class ClassificacoesField(serializers.JSONField):
    def to_internal_value(self, data):
        validated_data = []

        if len(data) == 0:
            msg = u"Os dados das classificações são obrigatórios."
            raise serializers.ValidationError(msg)

        for item in data:
            if isinstance(item, str):
                continue
            if item.get('atuacao') in [None, ""]:
                msg = u"Insira uma atuação correta."
                raise serializers.ValidationError(msg)
            if item.get('area') in [None, ""]:
                msg = u"Escolha uma das áreas disponiveis."
                raise serializers.ValidationError(msg)
            if item.get('estilo') in [None, ""]:
                msg = u"Escolha um dos estilos disponíveis."
                raise serializers.ValidationError(msg)
            if item.get('experiencia') in [None, ""]:
                msg = u"Insira o seu tempo de experiência."
                raise serializers.ValidationError(msg)

        return data
