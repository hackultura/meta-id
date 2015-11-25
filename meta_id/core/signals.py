# -*- coding: utf-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Documento


@receiver(post_save, sender=Documento)
def register_content_by_ente_or_profile(sender, instance, created, **kwargs):
    """
    Captura os metadados e uid do documento inserido e salva
    no campo JSON do modelo de ente ou perfil.
    """
    if not isinstance(instance.owner.documentos, list):
        instance.owner.documentos = []

    filename = instance.arquivo.name.split("/")[-1]
    filename, format = filename.split(".")
    instance.owner.documentos.append({
        "nome": instance.nome,
        "arquivo": filename,
        "formato": format,
        "tamanho": instance.arquivo.size,
        "enviado_em": instance.criado_em,
        "vencimento": instance.vencimento
    })
    instance.owner.save()
