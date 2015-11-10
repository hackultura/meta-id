# -*- coding: utf-8 -*-

try:
    from StringIO import StringIO
except Exception as e:
    from io import StringIO

from PIL import Image

from django.core.files.base import ContentFile


def dummy_image(name='image_test', format='png', enable_imagefield=True):
    """Gera um imagem para 'mockar' nos testes. Você pode passar
    os seguintes parametros::
        :param name:
            Nome da Imagem. Padrão: ``image_test``
        :param format:
            Formato da Imagem (PNG, JPG, etc): Padrão: ``png``
        :param enable_imagefield:
            Habilita/Desabilita o tratamento de um arquivo pelo django.
            Padrão: True
    """
    file_obj = StringIO()
    image = Image.new("RGBA", size=(50, 50))
    image.save(file_obj, format)
    file_obj.seek(0)

    if enable_imagefield:
        file_obj = ContentFile(file_obj.read())
        file_obj.name = name
    return file_obj
