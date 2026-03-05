# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=15)),
                ('time', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('task_id', models.CharField(blank=True, editable=False, max_length=50)),
                ('time_zone', timezone_field.fields.TimeZoneField(default='US/Pacific')),
            ],
        ),
    ]
