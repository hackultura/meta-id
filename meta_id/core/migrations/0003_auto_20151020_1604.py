# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_add_classifications_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilartistico',
            name='historico',
            field=models.CharField(default='', max_length=255, verbose_name='Breve Histórico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfilartistico',
            name='nome',
            field=models.CharField(default='', max_length=60, verbose_name='Nome Artístico'),
            preserve_default=False,
        ),
    ]
