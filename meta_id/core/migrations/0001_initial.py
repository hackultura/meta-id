# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.serializers.json
import decimal
import uuid
import django.contrib.postgres.fields
from django.conf import settings
import postgres.fields
import django_extensions.db.fields
import meta_id.core.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoArtistica',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('area', models.CharField(max_length=100, verbose_name='Area Artistica')),
                ('estilos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
            name='Ente',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('informacoes_geograficas', postgres.fields.JSONField(null=True, decode_kwargs={'parse_float': decimal.Decimal}, blank=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
                ('telefone', postgres.fields.JSONField(null=True, decode_kwargs={'parse_float': decimal.Decimal}, blank=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('nascimento', models.DateField()),
                ('classificacoes', postgres.fields.JSONField(decode_kwargs={'parse_float': decimal.Decimal}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
                ('documentos', postgres.fields.JSONField(decode_kwargs={'parse_float': decimal.Decimal}, blank=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ente',
                'verbose_name_plural': 'entes',
            },
        ),
        migrations.CreateModel(
            name='PerfilArtistico',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nome', models.CharField(max_length=60, verbose_name='Nome Artístico')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, overwrite=True, editable=False, populate_from='nome')),
                ('historico', models.CharField(max_length=255, verbose_name='Breve Histórico')),
                ('ente', models.ForeignKey(to='core.Ente', related_name='perfis')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('perfil', models.ForeignKey(to='core.PerfilArtistico')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioArquivo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('arquivo', models.FileField(upload_to=meta_id.core.models.generate_portfolio_filepath)),
                ('perfil', models.ForeignKey(to='core.PerfilArtistico')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('audio', models.FileField(upload_to=meta_id.core.models.generate_portfolio_filepath)),
                ('perfil', models.ForeignKey(to='core.PerfilArtistico')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioImagem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('imagem', models.ImageField(upload_to=meta_id.core.models.generate_portfolio_filepath)),
                ('descricao', models.CharField(max_length=255)),
                ('perfil', models.ForeignKey(to='core.PerfilArtistico')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioImagemAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('imagem', models.ImageField(upload_to=meta_id.core.models.generate_portfolio_filepath)),
                ('album', models.ForeignKey(to='core.PortfolioAlbum', related_name='fotos')),
                ('perfil', models.ForeignKey(to='core.PerfilArtistico')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
                ('plataforma', models.CharField(max_length=30, choices=[('youtube', 'Youtube'), ('vimeo', 'Vimeo')])),
                ('perfil', models.ForeignKey(to='core.PerfilArtistico')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('num_ceac', models.AutoField(serialize=False, verbose_name='Numero de Registro de CEAC', primary_key=True)),
                ('ente', models.ForeignKey(to='core.Ente')),
            ],
            options={
                'verbose_name': 'registro',
                'verbose_name_plural': 'registros',
            },
        ),
        migrations.AddField(
            model_name='documento',
            name='perfil',
            field=models.ForeignKey(to='core.PerfilArtistico'),
        ),
    ]
