# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160506_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='portfolioalbum',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='portfolioimagemalbum',
            name='perfil',
        ),
        migrations.AlterField(
            model_name='portfolioarquivo',
            name='perfil',
            field=models.ForeignKey(related_name='arquivos', to='core.PerfilArtistico'),
        ),
        migrations.AlterField(
            model_name='portfolioaudio',
            name='perfil',
            field=models.ForeignKey(related_name='audios', to='core.PerfilArtistico'),
        ),
        migrations.AlterField(
            model_name='portfolioimagem',
            name='perfil',
            field=models.ForeignKey(related_name='imagens', to='core.PerfilArtistico'),
        ),
        migrations.AlterField(
            model_name='portfoliovideo',
            name='perfil',
            field=models.ForeignKey(related_name='videos', to='core.PerfilArtistico'),
        ),
    ]
