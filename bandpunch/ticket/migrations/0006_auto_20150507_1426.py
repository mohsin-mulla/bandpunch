# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_venue_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='events',
        ),
        migrations.AddField(
            model_name='event',
            name='artists',
            field=models.ManyToManyField(to='ticket.Artist'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone_number',
            field=models.CharField(blank=True, null=True, max_length=11, validators=[django.core.validators.RegexValidator(regex='^\\d{11}$', code='Invalid number', message='Length has to be 11')]),
            preserve_default=True,
        ),
    ]
