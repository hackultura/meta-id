# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_add_classifications_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliovideo',
            name='plataforma',
            field=models.CharField(max_length=30),
        ),
    ]
