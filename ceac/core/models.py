from django.conf import settings
from django.db import models

from django.utils.translation import ugettext_lazy as _


DECISAO_ANALISE = (
    (1, 'Favorável'),
    (2, 'Em Diligência'),
    (3, 'Desfavorável'),
)


class Ente(models.Model):
    nome = models.CharField(_('Nome'), max_length=100, blank=False)
    nome_artistico = models.CharField(_('Nome Artistico'), max_length=150)
    cpfcnpj = models.IntegerField(_('CPF/CPNJ'), max_length=12, unique=True, blank=False)
    processo = models.IntegerField(_('Numero do Processo'), max_length=14, unique=True, blank=True)
    dt_abertura_processo = models.DateField(_('Data de abertura do Processo'))

    class Meta:
        verbose_name = "ente"
        verbose_name_plural = "entes"


class Registro(models.Model):
    num_ceac = models.AutoFieldField(_('Numero de Registro de CEAC'))
    ente = models.ForeignKey(Ente)

    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "registros"

