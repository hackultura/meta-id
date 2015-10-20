# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parecer',
            name='decisao',
            field=models.IntegerField(verbose_name='Decisão do parecerista', choices=[(1, 'Favorável'), (2, 'Em Diligência'), (3, 'Desfavorável')]),
        ),
    ]
