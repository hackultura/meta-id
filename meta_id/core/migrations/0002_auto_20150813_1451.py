# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ente',
            name='cpfcnpj',
            field=models.BigIntegerField(max_length=12, unique=True, verbose_name='CPF/CPNJ'),
        ),
        migrations.AlterField(
            model_name='ente',
            name='processo',
            field=models.BigIntegerField(max_length=14, unique=True, verbose_name='Numero do Processo', blank=True),
        ),
    ]
