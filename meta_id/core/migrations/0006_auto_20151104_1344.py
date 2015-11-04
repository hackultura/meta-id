# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django.core.serializers.json
import decimal
import datetime
import postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_ente_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilartistico',
            name='atuacao',
        ),
        migrations.RemoveField(
            model_name='perfilartistico',
            name='classificacao',
        ),
        migrations.RemoveField(
            model_name='perfilartistico',
            name='experiencia',
        ),
        migrations.AddField(
            model_name='ente',
            name='classificacoes',
            field=postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, default={}, decode_kwargs={'parse_float': decimal.Decimal}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ente',
            name='cpf',
            field=models.CharField(default='', max_length=15, verbose_name='CPF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ente',
            name='nascimento',
            field=models.DateField(default=datetime.datetime(2015, 11, 4, 15, 44, 30, 785526, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
