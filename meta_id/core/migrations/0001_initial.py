# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import decimal
import postgres.fields
import uuid
import django.core.serializers.json
import django.core.validators
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoArtistica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('area', models.CharField(max_length=100, verbose_name='Area Artistica')),
                ('estilos', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(max_length=255))),
            ],
        ),
        migrations.CreateModel(
            name='Ente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('informacoes_geograficas', postgres.fields.JSONField(blank=True, null=True, decode_kwargs={'parse_float': decimal.Decimal}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
                ('telefone', postgres.fields.JSONField(blank=True, null=True, decode_kwargs={'parse_float': decimal.Decimal}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
            ],
            options={
                'verbose_name_plural': 'entes',
                'verbose_name': 'ente',
            },
        ),
        migrations.CreateModel(
            name='PerfilArtistico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('atuacao', models.CharField(choices=[('gestao', 'Gestão'), ('pesquisa', 'Pesquisa'), ('facilitacao_formacao', 'Facilitação/Formação'), ('producao', 'Produção'), ('criacao_desenv', 'Criação/Desenvolvimento Artístico'), ('suporte', 'Suporte Técnico')], max_length=35, verbose_name='Atuação Cultural')),
                ('classificacao', postgres.fields.JSONField(decode_kwargs={'parse_float': decimal.Decimal}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
                ('experiencia', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('ente', models.ForeignKey(related_name='perfis', to='core.Ente')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('num_ceac', models.AutoField(primary_key=True, serialize=False, verbose_name='Numero de Registro de CEAC')),
                ('ente', models.ForeignKey(to='core.Ente')),
            ],
            options={
                'verbose_name_plural': 'registros',
                'verbose_name': 'registro',
            },
        ),
    ]
