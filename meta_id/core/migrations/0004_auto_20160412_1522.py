# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_perfilartistico_documentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioalbum',
            name='dono',
            field=models.UUIDField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioarquivo',
            name='dono',
            field=models.UUIDField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioaudio',
            name='dono',
            field=models.UUIDField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioimagem',
            name='dono',
            field=models.UUIDField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioimagemalbum',
            name='dono',
            field=models.UUIDField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliovideo',
            name='dono',
            field=models.UUIDField(default=''),
            preserve_default=False,
        ),
    ]
