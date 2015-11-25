# -*- coding: utf-8 -*-

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Documento


def _search_document(documentos, file):
    file = file.split("/")[-1]
    filename, format = file.split(".")

    for documento in documentos:
        if documento.get("arquivo") == filename:
            return documento
    return None


@receiver(post_save, sender=Documento)
def register_content_by_ente_or_profile(sender, instance, created, **kwargs):
    """
    Captura os metadados e uid do documento inserido e salva
    no campo JSON do modelo de ente ou perfil.
    """
    owner = instance._get_owner()
    if not isinstance(owner.documentos, list):
        owner.documentos = []

    filename = instance.arquivo.name.split("/")[-1]
    filename, format = filename.split(".")
    owner.documentos.append({
        "nome": instance.nome,
        "arquivo": filename,
        "formato": format,
        "tamanho": instance.arquivo.size,
        "enviado_em": instance.criado_em,
        "vencimento": instance.vencimento
    })
    owner.save()


# TODO: Fique registrado se caso essa tarefa for custosa
# pela quantidade de documentos futuramente, considere isso
# uma tarefa para o celery.
@receiver(pre_delete, sender=Documento)
def remove_content_of_owner(sender, instance, **kwargs):
    """
    Antes da remocao do conteudo, ele e retirado do JSON
    de documentacao do ente ou perfil.
    """
    owner = instance._get_owner()
    documentos = owner.documentos
    resultado = _search_document(documentos, instance.arquivo.name)
    documentos.remove(resultado)
    owner.documentos = documentos
    owner.save()
