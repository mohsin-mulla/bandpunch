# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0011_auto_20150508_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='curfew_time',
            field=models.TimeField(),
            preserve_default=True,
        ),
    ]
