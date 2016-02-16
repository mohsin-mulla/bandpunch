# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20150507_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='venues',
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(default='', to='ticket.Venue'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='capacity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
