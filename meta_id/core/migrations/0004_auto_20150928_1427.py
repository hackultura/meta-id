# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150813_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ente',
            name='cpfcnpj',
        ),
        migrations.RemoveField(
            model_name='ente',
            name='dt_abertura_processo',
        ),
        migrations.RemoveField(
            model_name='ente',
            name='nome_artistico',
        ),
        migrations.RemoveField(
            model_name='ente',
            name='processo',
        ),
    ]
