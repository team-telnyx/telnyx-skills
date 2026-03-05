from automated_survey.models import Survey, Question
from django.test import TestCase
from django.core.management import call_command


class SurveyLoaderTest(TestCase):
    def test_load_survey(self):
        call_command('load_survey', 'automated_survey/tests/fixtures/bear_survey.json')

        all_surveys = Survey.objects.all()
        all_questions = Question.objects.all()

        assert len(all_surveys) == 1
        assert len(all_questions) == 5
        assert all_surveys.first().title == 'About bears'
