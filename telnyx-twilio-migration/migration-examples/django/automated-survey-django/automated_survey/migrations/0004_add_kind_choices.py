# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automated_survey', '0003_load_bear_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='kind',
            field=models.CharField(choices=[('text', 'Text'), ('yes-no', 'Yes or no'), ('numeric', 'Numeric')], max_length=255),
        ),
    ]
