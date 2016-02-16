# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_event_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
