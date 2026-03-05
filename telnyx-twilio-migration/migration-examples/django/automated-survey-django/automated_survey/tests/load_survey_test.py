import pytest

from automated_survey.models import Survey, Question
from automated_survey.util import SurveyLoader
from django.test import TestCase

sample_survey = """
{\"questions\":[{\"body\":\"What type of bear is best?\",\"kind\":\"text\"},{\"body\":\"In a scale of 1 to 10, how cute do you find koalas?\",\"kind\":\"numeric\"},{\"body\":\"Do you think bears beat beets?\",\"kind\":\"yes-no\"},{\"body\":\"What's the relationship between Battlestar Galactica and bears?\",\"kind\":\"text\"},{\"body\":\"Do sloths qualify as bears?\",\"kind\":\"text\"}],\"title\":\"About bears\"}\"'\"}\"\"]\"\"}
"""

broken_survey = """
{\"questions\":[{\"\":\"What type of bear is best?\",\"kind\":\"text\"},{\"\":\"In a scale of 1 to 10, how cute do you find koalas?\",\"kind\":\"numeric\"},{\"body\":\"Do you think bears beat beets?\",\"kind\":\"yes-no\"},{\"body\":\"What's the relationship between Battlestar Galactica and bears?\",\"kind\":\"text\"},{\"body\":\"Do sloths qualify as bears?\",\"kind\":\"text\"}],\"title\":\"About bears\"}\"'\"}\"\"]\"\"}
"""


class SurveyLoaderTest(TestCase):
    def load_survey_test(self):
        loader = SurveyLoader(sample_survey)
        loader.load_survey()

        all_surveys = Survey.objects.all()
        all_questions = Question.objects.all()

        assert len(all_surveys) == 1
        assert len(all_questions) == 5
        assert all_surveys.first().title == 'About bears'

        with pytest.raises(KeyError):
            loader = SurveyLoader(broken_survey)
            loader.load_survey()
