import uuid
# from django.conf import settings
from django.db import models

from django.core.urlresolvers import reverse

from django.utils.translation import ugettext_lazy as _


class Ente(models.Model):
    id_pub = models.UUIDField(default=uuid.uuid4, editable=False)
    nome = models.CharField(_('Nome'), max_length=100, blank=False)
    endereco = models.TextField(_('Endereço'), blank=True)
    bairro = models.TextField(_('Bairro'), blank=True)
    uf = models.TextField(_('UF'), blank=True)
    cep = models.TextField(_('CEP'), blank=True)


    class Meta:
        verbose_name = "ente"
        verbose_name_plural = "entes"

    def __str__(self):
        return self.nome

    def get_absolute_url():
        return reverse('core.views.entes', args=[str(self.id)])


class Registro(models.Model):
    num_ceac = models.AutoField(
        _('Numero de Registro de CEAC'),
        primary_key=True
    )
    ente = models.ForeignKey(Ente)

    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "registros"

    def __str__(self):
        return self.num_ceac

    def get_absolute_url():
        return reverse('core.views.registros')
