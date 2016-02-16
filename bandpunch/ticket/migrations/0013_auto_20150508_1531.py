# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0012_auto_20150508_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='curfew_time',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
