# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardChoices',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('payment_type', models.CharField(default=None, max_length=30, unique=True)),
            ],
            options={
                'ordering': ['payment_type'],
                'verbose_name_plural': 'payment types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('genre', models.CharField(default=None, max_length=30, unique=True)),
            ],
            options={
                'ordering': ['genre'],
                'verbose_name_plural': 'genres',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(validators=[django.core.validators.RegexValidator(regex='^\\d{10}$', code='Invalid number', message='Length has to be 11')], max_length=11, unique=True)),
                ('email', models.EmailField(validators=[django.core.validators.EmailValidator()], max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='event',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['name'], 'verbose_name_plural': 'artists'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['name'], 'verbose_name_plural': 'events'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'ordering': ['name'], 'verbose_name_plural': 'venues'},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='time',
            new_name='time_start',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='event',
        ),
        migrations.RemoveField(
            model_name='event',
            name='venue',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='artist',
            name='events',
            field=models.ManyToManyField(to='ticket.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(default=None, to='ticket.Genre', related_name='genres'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(default=None, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='19:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=None, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='time_curfew',
            field=models.TimeField(default='19:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time_end',
            field=models.TimeField(default='19:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='venues',
            field=models.ManyToManyField(to='ticket.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='cash_only',
            field=models.BooleanField(default=False, verbose_name='Cash only'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateField(default=datetime.datetime.now, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='delivery_option',
            field=models.BooleanField(default=True, verbose_name='Is Collecting Ticket'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='reference_number',
            field=models.CharField(default=None, max_length=16, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='temp_session_key',
            field=models.CharField(null=True, default=None, editable=False, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='venue',
            name='slug',
            field=models.SlugField(default=None, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='card_name',
            field=models.CharField(default=None, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9\\s]*$', 'Only alphanumeric characters are allowed.')], max_length=26),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='card_number',
            field=models.CharField(default=None, max_length=19),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='payment_type',
            field=models.ForeignKey(to='ticket.CardChoices', related_name='Payment Types'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='security_code',
            field=models.IntegerField(default=None, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(default=None, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venue',
            name='capacity',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone_number',
            field=models.IntegerField(default=None, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$', code='Invalid number', message='Length has to be 11')], max_length=11, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venue',
            name='website',
            field=models.URLField(null=True, max_length=50),
            preserve_default=True,
        ),
    ]
