# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import six
import base64
import uuid

from django.utils import timezone
from django.core.files.base import ContentFile

from rest_framework import serializers


class EnderecoField(serializers.JSONField):
    def to_internal_value(self, data):
        validated_data = []


        for item in data:
            if isinstance(item, six.string_types):
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

            if not isinstance(item, six.string_types):
                item["adicionado_em"] = timezone.now()
            validated_data.append(item)

        return validated_data


class TelefoneField(serializers.JSONField):
    def to_internal_value(self, data):
        validated_data = []

        for item in data:
            if isinstance(item, six.string_types):
                continue
            else:
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
            if isinstance(item, six.string_types):
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


class FileUploadJSONField(serializers.JSONField):
    def to_internal_value(self, data):

        for item in data:
            if isinstance(item, six.string_types):
                continue
            if item.get('tamanho') in [None, ""]:
                msg = u"Defina o tamanho do arquivo (em bytes)."
                raise serializers.ValidationError(msg)
            if item.get('nome_arquivo') in [None, ""]:
                msg = u"Defina o nome do arquivo."
                raise serializers.ValidationError(msg)
            if item.get('formato') in [None, ""]:
                msg = u"Defina o formato válido, no padrão MIME."
                raise serializers.ValidationError(msg)
            if item.get('base64') in [None, ""]:
                msg = u"Envie o arquivo no formato base64."
                raise serializers.ValidationError(msg)

            # Validando o formato base64
            base64_pattern = r'(?:[A-Za-z0-9+/]{4}){2,}(?:[A-Za-z0-9+/]{2}' \
            '[AEIMQUYcgkosw048]=|[A-Za-z0-9+/][AQgw]==)'

            if re.search(base64_pattern, item.get('base64')) is None:
                msg = u"Envie um arquivo com formato base64 válido."
                raise serializers.ValidationError(msg)

        return data


class FileBase64Field(serializers.FileField):
    def to_internal_value(self, data):
        if data.get('tamanho') in [None, ""]:
            msg = u"Defina o tamanho do arquivo (em bytes)."
            raise serializers.ValidationError(msg)
        if data.get('nome_arquivo') in [None, ""]:
            msg = u"Defina o nome do arquivo."
            raise serializers.ValidationError(msg)
        if data.get('formato') in [None, ""]:
            msg = u"Defina o formato válido, no padrão MIME."
            raise serializers.ValidationError(msg)
        if data.get('base64') in [None, ""]:
            msg = u"Envie o arquivo no formato base64."
            raise serializers.ValidationError(msg)

        # Validando o formato base64
        base64_pattern = r'(?:[A-Za-z0-9+/]{4}){2,}(?:[A-Za-z0-9+/]{2}' \
        '[AEIMQUYcgkosw048]=|[A-Za-z0-9+/][AQgw]==)'

        if re.search(base64_pattern, data.get('base64')) is None:
            msg = u"Envie um arquivo com formato base64 válido."
            raise serializers.ValidationError(msg)

        if isinstance(data, dict):
            id = uuid.uuid4()
            content, ext = data.get('formato').split("/")
            data = ContentFile(base64.b64decode(data.get('base64')),
                               name=id.urn[9:] + '.' + ext)
        return super(FileBase64Field, self).to_internal_value(data)
