# from django.conf import settings
from django.db import models

from django.core.urlresolvers import reverse

from django.utils.translation import ugettext_lazy as _


class Ente(models.Model):
    nome = models.CharField(_('Nome'), max_length=100, blank=False)
    # nome_artistico = models.CharField(_('Nome Artistico'), max_length=150)
    # cpfcnpj = models.BigIntegerField(_('CPF/CPNJ'), max_length=12, unique=True, blank=False)
    # processo = models.BigIntegerField(_('Numero do Processo'), max_length=14, unique=True, blank=True, null=True)
    # dt_abertura_processo = models.DateField(_('Data de abertura do Processo'))

    class Meta:
        verbose_name = "ente"
        verbose_name_plural = "entes"

    def __str__(self):
        return self.nome

    def get_absolute_url():
        return reverse('core.views.entes', args=[str(self.id)])


class Registro(models.Model):
    num_ceac = models.AutoField(_('Numero de Registro de CEAC'), primary_key=True)
    ente = models.ForeignKey(Ente)

    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "registros"

    def __str__(self):
        return self.num_ceac

    def get_absolute_url():
        return reverse('core.views.registros')
