# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import postgres.fields
import decimal
import django.core.serializers.json


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parecer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('texto_parecer', models.TextField(verbose_name='Parecer')),
                ('decisao', models.IntegerField(choices=[(1, 'Favorável'), (2, 'Em Diligência'), (3, 'Desfavorável')], verbose_name='Decisão do parecerista')),
                ('data_decisao', models.DateField(verbose_name='Data da Decisão')),
                ('areas_atuacao', postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal}, verbose_name='Áreas de Atuação')),
            ],
            options={
                'verbose_name': 'analise',
                'verbose_name_plural': 'analises',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('data_pedido', models.DateField(verbose_name='Data do Pedido')),
                ('areas_atuacao', postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal}, verbose_name='Áreas de Atuação')),
                ('ente', models.ForeignKey(to='core.Ente')),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
