# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150813_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ente',
            name='processo',
            field=models.BigIntegerField(blank=True, unique=True, verbose_name='Numero do Processo', null=True, max_length=14),
        ),
    ]
