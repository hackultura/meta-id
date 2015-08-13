# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('nome_artistico', models.CharField(max_length=150, verbose_name='Nome Artistico')),
                ('cpfcnpj', models.IntegerField(max_length=12, unique=True, verbose_name='CPF/CPNJ')),
                ('processo', models.IntegerField(max_length=14, verbose_name='Numero do Processo', unique=True, blank=True)),
                ('dt_abertura_processo', models.DateField(verbose_name='Data de abertura do Processo')),
            ],
            options={
                'verbose_name_plural': 'entes',
                'verbose_name': 'ente',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('num_ceac', models.AutoField(verbose_name='Numero de Registro de CEAC', primary_key=True, serialize=False)),
                ('ente', models.ForeignKey(to='core.Ente')),
            ],
            options={
                'verbose_name_plural': 'registros',
                'verbose_name': 'registro',
            },
        ),
    ]
