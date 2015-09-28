# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150928_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='ente',
            name='id_pub',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
