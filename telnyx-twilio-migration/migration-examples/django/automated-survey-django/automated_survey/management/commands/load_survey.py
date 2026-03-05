import os
from django.core.management import BaseCommand
from automated_survey.util import SurveyLoader

root = os.path.abspath(os.path.dirname(__name__))


class Command(BaseCommand):
    COMMAND = 'load_surveys'

    def add_arguments(self, parser):
        parser.add_argument(self.COMMAND, metavar='survey-name', nargs=1)

    def handle(self, *args, **options):
        file_name = options['load_surveys'][0]
        absolute_file_name = os.path.join(str(root), file_name)

        with open(absolute_file_name, 'r') as survey_to_load:
            loader = SurveyLoader(survey_to_load.read())
            loader.load_survey()
