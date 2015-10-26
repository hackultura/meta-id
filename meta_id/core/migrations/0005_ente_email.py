# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151022_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='ente',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail', default=''),
            preserve_default=False,
        ),
    ]
