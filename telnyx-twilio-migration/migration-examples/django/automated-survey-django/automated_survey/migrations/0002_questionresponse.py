# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automated_survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response', models.CharField(max_length=255)),
                ('call_sid', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('question', models.ForeignKey(to='automated_survey.Question', on_delete=models.CASCADE)),
            ],
        ),
    ]
