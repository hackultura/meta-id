from django.conf import settings
from django.db import models

from django.utils.translation import ugettext_lazy as _

from postgres import fields


DECISAO_ANALISE = (
    (1, 'Favorável'),
    (2, 'Em Diligência'),
    (3, 'Desfavorável'),
)


class Pedido(models.Model):
    ente = models.ForeignKey('core.Ente')
    data_pedido = models.DateField(_('Data do Pedido'))
    areas_atuacao = fields.JSONField(_('Áreas de Atuação'))

    class Meta:
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"

    def get_absolute_url():
        return reverse('pedido.views.details', args=[str(self.id)])


class Parecer(models.Model):
    pedido = models.ForeignKey(Pedido)
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    texto_parecer = models.TextField(_('Parecer'))
    decisao = models.IntegerField(_('Decisão do parecerista'), choices=DECISAO_ANALISE)
    data_decisao = models.DateField(_('Data da Decisão'))
    areas_atuacao = fields.JSONField(_('Áreas de Atuação'))

    class Meta:
        verbose_name = "analise"
        verbose_name_plural = "analises"

    def get_absolute_url(self):
        return reverse('parecer.views.details', args=[str(self.id)])

