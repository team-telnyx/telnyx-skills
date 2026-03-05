# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def load_bear_survey(apps, schema_editor):
    Survey = apps.get_model('automated_survey', 'Survey')
    Question = apps.get_model('automated_survey', 'Question')
    
    if Survey.objects.filter(title='About bears').exists():
        return
    
    survey = Survey.objects.create(title='About bears')
    
    questions = [
        {'body': 'What type of bear is best?', 'kind': 'text'},
        {'body': 'In a scale of 1 to 10, how cute do you find koalas?', 'kind': 'numeric'},
        {'body': 'Do you think bears beat beets?', 'kind': 'yes-no'},
        {'body': "What's the relationship between Battlestar Galactica and bears?", 'kind': 'text'},
        {'body': 'Do sloths qualify as bears?', 'kind': 'text'},
    ]
    
    for q in questions:
        Question.objects.create(survey=survey, body=q['body'], kind=q['kind'])


def unload_bear_survey(apps, schema_editor):
    Survey = apps.get_model('automated_survey', 'Survey')
    Survey.objects.filter(title='About bears').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('automated_survey', '0002_questionresponse'),
    ]

    operations = [
        migrations.RunPython(load_bear_survey, unload_bear_survey),
    ]
