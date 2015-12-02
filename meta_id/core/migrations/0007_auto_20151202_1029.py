# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import meta_id.core.models
import postgres.fields
import decimal
import django.core.serializers.json
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151104_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('dono', models.UUIDField()),
                ('nome', models.CharField(max_length=255)),
                ('vencimento', models.DateField()),
                ('arquivo', models.FileField(upload_to='documentacao/%Y/%m/%d')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioAlbum',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioArquivo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('arquivo', models.FileField(upload_to=meta_id.core.models.generate_portfolio_filepath)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioAudio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('audio', models.FileField(upload_to=meta_id.core.models.generate_portfolio_filepath)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioImagem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('imagem', models.ImageField(upload_to=meta_id.core.models.generate_portfolio_filepath)),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioImagemAlbum',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('imagem', models.ImageField(upload_to=meta_id.core.models.generate_portfolio_filepath)),
                ('album', models.ForeignKey(to='core.PortfolioAlbum', related_name='fotos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioVideo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
                ('plataforma', models.CharField(choices=[('youtube', 'Youtube'), ('vimeo', 'Vimeo')], max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ente',
            name='documentos',
            field=postgres.fields.JSONField(blank=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal}),
        ),
    ]
