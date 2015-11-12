# -*- coding: utf-8 -*-

import base64
import os

try:
    from StringIO import StringIO
except Exception as e:
    from io import StringIO

from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile


def dummy_file(name='file_test', format='txt', **kwargs):
    """
    Gera um arquivo para 'mockar' nos testes. Você pode
    passar os seguintes parametros:
        :param name:
            Nome do Arquivo
        :param format:
            Extensao do Arquivo. Padrão: .txt
        :param content:
            Define o conteudo do arquivo. Padrão: 'Dummy Content'
        :param enable_filefield:
            Habilita/Desabilita o tratamento de um arquivo pelo django.
            Padrão: True
    """
    content = kwargs.pop('content', "Dummy Content")
    enable_filefield = kwargs.pop('enable_filefield', True)
    content_type = kwargs.pop('content_type', None)

    file_obj = StringIO()
    file_obj.write(content)
    file_obj.seek(0, os.SEEK_END)

    if enable_filefield:
        file_obj = ContentFile(file_obj.read())
        file_obj.name = "{0}.{1}".format(name, format)

    return file_obj


def dummy_base64_file(name='file_test', format='csv', **kwargs):
    """
    Gera um arquivo para 'mockar' nos testes, mas em formato base64. Você pode
    passar os seguintes parametros:
        :param name:
            Nome do Arquivo
        :param format:
            Extensao do Arquivo. Padrão: .csv
        :param content:
            Define o conteudo do arquivo. Padrão: 'Dummy,Content'
        :param content_type:
            Define o conteudo do arquivo, usando formato MIME.

    O resultado gerado, será um JSON, com a seguinte estrutura:

        {
            "tamanho": 10290 (em bytes),
            "formato": "text/csv",
            "nome_arquivo": "file_test.csv",
            "base64": "/019lasdjaslk19aslASdlk12-ASLKDJ123//ASDLAKj=="
        }
    """
    content = kwargs.pop('content', "Dummy,Content")
    content_type = kwargs.pop('content_type', "text/csv")
    filename = "{0}.{1}".format(name, format)

    file_obj = StringIO()
    file_obj.write(content)
    file_obj.seek(0, os.SEEK_END)

    data = base64.b64encode(content.encode()).decode("utf-8")
    filesize = file_obj.tell()

    data_file = {}
    data_file["tamanho"] = filesize
    data_file["formato"] = content_type
    data_file["nome_arquivo"] = filename
    data_file["base64"] = data

    return data_file
