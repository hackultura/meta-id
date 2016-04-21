# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import decimal
import django.core.serializers.json
import postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_add_classifications_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilartistico',
            name='documentos',
            field=postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, default={}, decode_kwargs={'parse_float': decimal.Decimal}),
            preserve_default=False,
        ),
    ]
