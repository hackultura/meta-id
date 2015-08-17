# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.serializers.json
import decimal
from django.conf import settings
import postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parecer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('texto_parecer', models.TextField(verbose_name='Parecer')),
                ('decisao', models.IntegerField(max_length=1, choices=[(1, 'Favorável'), (2, 'Em Diligência'), (3, 'Desfavorável')], verbose_name='Decisão do parecerista')),
                ('data_decisao', models.DateField(verbose_name='Data da Decisão')),
                ('areas_atuacao', postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal}, verbose_name='Áreas de Atuação')),
            ],
            options={
                'verbose_name_plural': 'analises',
                'verbose_name': 'analise',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('data_pedido', models.DateField(verbose_name='Data do Pedido')),
                ('areas_atuacao', postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal}, verbose_name='Áreas de Atuação')),
                ('ente', models.ForeignKey(to='core.Ente')),
            ],
            options={
                'verbose_name_plural': 'pedidos',
                'verbose_name': 'pedido',
            },
        ),
        migrations.AddField(
            model_name='parecer',
            name='pedido',
            field=models.ForeignKey(to='analise.Pedido'),
        ),
        migrations.AddField(
            model_name='parecer',
            name='responsavel',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
