# -*- coding: utf-8 -*-

try:
    from StringIO import StringIO
except Exception as e:
    from io import StringIO

from django.core.files.base import ContentFile


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

    file_obj = StringIO()
    file_obj.write(content)
    file_obj.seek(0)

    if enable_filefield:
        file_obj = ContentFile(file_obj.read())
        file_obj.name = "{0}.{1}".format(name, format)
    return file_obj
