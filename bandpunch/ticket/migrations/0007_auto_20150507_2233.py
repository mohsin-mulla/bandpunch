# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_auto_20150507_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='ticket',
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
