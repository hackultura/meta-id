from django.conf import settings
from django.db import models

from django.utils.translation import ugettext_lazy as _


class Analise(models.Model):
    ente = models.ForeignKey('core.Ente')
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    texto_parecer = models.TextField(_('Parecer'))
    decisao = models.IntegerField(_('Decisão do parecerista'), max_length=1, choices=DECISAO_ANALISE)
    data_decisao = models.DateField(_('Data da Decisão'), auto_add=True)

    class Meta:
        verbose_name = "analise"
        verbose_name_plural = "analises"

    def get_absolute_url(self):
        return reverse('analise.views.details', args=[str(self.id)])

