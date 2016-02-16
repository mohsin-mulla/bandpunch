# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0009_auto_20150508_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='', upload_to='event/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.ImageField(default='', upload_to='venue/images'),
            preserve_default=False,
        ),
    ]
