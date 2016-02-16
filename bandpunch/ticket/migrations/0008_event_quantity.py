# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_auto_20150507_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
