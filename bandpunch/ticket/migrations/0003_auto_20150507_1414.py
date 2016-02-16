# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20150507_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='time_curfew',
            new_name='curfew_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='time_end',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='time_start',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(default='', upload_to='artist/images'),
            preserve_default=False,
        ),
    ]
