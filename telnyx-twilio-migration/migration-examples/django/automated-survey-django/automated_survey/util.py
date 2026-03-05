import json
from automated_survey.models import Survey, Question


class SurveyLoader(object):

    def __init__(self, survey_content):
        self.survey = json.loads(survey_content)

    def load_survey(self):
        new_survey = Survey(title=self.survey['title'])
        questions = [Question(body=question['body'],
                              kind=question['kind'])
                     for question in self.survey['questions']]
        new_survey.save()
        new_survey.question_set.add(*questions)
