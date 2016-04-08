# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import postgres.fields
import decimal
import django.contrib.postgres.fields
import uuid
import meta_id.core.models
import django_extensions.db.fields
import django.core.serializers.json
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoArtistica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100, verbose_name='Area Artistica')),
                ('estilos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('informacoes_geograficas', postgres.fields.JSONField(blank=True, null=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('telefone', postgres.fields.JSONField(blank=True, null=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('nascimento', models.DateField()),
                ('classificacoes', postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('documentos', postgres.fields.JSONField(blank=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'entes',
                'verbose_name': 'ente',
            },
        ),
        migrations.CreateModel(
            name='PerfilArtistico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nome', models.CharField(max_length=60, verbose_name='Nome Artístico')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, overwrite=True, populate_from='nome')),
                ('historico', models.CharField(max_length=255, verbose_name='Breve Histórico')),
                ('ente', models.ForeignKey(related_name='perfis', to='core.Ente')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pub', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('imagem', models.ImageField(upload_to=meta_id.core.models.generate_portfolio_filepath)),
                ('album', models.ForeignKey(related_name='fotos', to='core.PortfolioAlbum')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
