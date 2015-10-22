# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151020_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='ente',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from='nome', blank=True, overwrite=True),
        ),
        migrations.AddField(
            model_name='perfilartistico',
            name='id_pub',
            field=models.UUIDField(editable=False, default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='perfilartistico',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from='nome', blank=True, overwrite=True),
        ),
    ]
