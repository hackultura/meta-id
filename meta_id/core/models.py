import uuid
# from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from postgres.fields import JSONField
from model_utils import Choices


class Ente(models.Model):
    id_pub = models.UUIDField(default=uuid.uuid4, editable=False)
    nome = models.CharField(_('Nome'), max_length=100, blank=False)
    informacoes_geograficas = JSONField(blank=True, null=True)
    telefone = JSONField(blank=True, null=True)

    class Meta:
        verbose_name = "ente"
        verbose_name_plural = "entes"

    def __str__(self):
        return self.nome

    def get_absolute_url():
        return reverse('core.views.entes', args=[str(self.id)])


class PerfilArtistico(models.Model):
    ATUACAO_CHOICES = Choices(
        ("gestao", _(u"Gestão")),
        ("pesquisa", _(u"Pesquisa")),
        ("facilitacao_formacao", _(u"Facilitação/Formação")),
        ("producao", _(u"Produção")),
        ("criacao_desenv", _(u"Criação/Desenvolvimento Artístico")),
        ("suporte", _(u"Suporte Técnico")),
    )

    ente = models.ForeignKey('Ente', related_name="perfis")
    atuacao = models.CharField(_(u"Atuação Cultural"), max_length=35,
                               choices=ATUACAO_CHOICES)
    classificacao = JSONField()
    experiencia = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )


class ClassificacaoArtistica(models.Model):
    area = models.CharField("Area Artistica", max_length=100)
    estilos = ArrayField(
        models.CharField(max_length=255)
    )


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
