# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import postgres.fields
import django.contrib.postgres.fields
import uuid
import django_extensions.db.fields
import meta_id.core.models
import decimal
import django.core.serializers.json


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoArtistica',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('area', models.CharField(verbose_name='Area Artistica', max_length=100)),
                ('estilos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
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
            name='Ente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('nome', models.CharField(verbose_name='Nome', max_length=100)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from='nome', editable=False, blank=True, overwrite=True)),
                ('informacoes_geograficas', postgres.fields.JSONField(decode_kwargs={'parse_float': decimal.Decimal}, blank=True, null=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
                ('telefone', postgres.fields.JSONField(decode_kwargs={'parse_float': decimal.Decimal}, blank=True, null=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
                ('email', models.EmailField(verbose_name='E-mail', max_length=254)),
                ('cpf', models.CharField(verbose_name='CPF', max_length=15)),
                ('nascimento', models.DateField()),
                ('classificacoes', postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('documentos', postgres.fields.JSONField(blank=True, decode_kwargs={'parse_float': decimal.Decimal}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
            ],
            options={
                'verbose_name_plural': 'entes',
                'verbose_name': 'ente',
            },
        ),
        migrations.CreateModel(
            name='PerfilArtistico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('nome', models.CharField(verbose_name='Nome Artístico', max_length=60)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from='nome', editable=False, blank=True, overwrite=True)),
                ('historico', models.CharField(verbose_name='Breve Histórico', max_length=255)),
                ('ente', models.ForeignKey(to='core.Ente', related_name='perfis')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioAlbum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('id_pub', models.UUIDField(editable=False, default=uuid.uuid4)),
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
