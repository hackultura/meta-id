# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_ente_id_pub'),
    ]

    operations = [
        migrations.AddField(
            model_name='ente',
            name='bairro',
            field=models.TextField(verbose_name='Bairro', blank=True),
        ),
        migrations.AddField(
            model_name='ente',
            name='cep',
            field=models.TextField(verbose_name='CEP', blank=True),
        ),
        migrations.AddField(
            model_name='ente',
            name='endereco',
            field=models.TextField(verbose_name='Endereço', blank=True),
        ),
        migrations.AddField(
            model_name='ente',
            name='uf',
            field=models.TextField(verbose_name='UF', blank=True),
        ),
    ]
