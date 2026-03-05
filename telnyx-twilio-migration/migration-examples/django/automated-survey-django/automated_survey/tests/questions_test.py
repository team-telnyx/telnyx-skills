from django.test import TestCase
from automated_survey.models import Survey, Question
from django.urls import reverse


class ShowQuestionTest(TestCase):

    def setUp(self):
        self.survey = Survey(title='A testing survey')
        self.survey.save()

        self.question = Question(body='A Question',
                                 kind=Question.TEXT,
                                 survey=self.survey)
        self.question.save()

        self.question_ids = {'survey_id': self.survey.id,
                             'question_id': self.question.id}

    def test_show_text_question_during_a_call(self):
        question_store_url = reverse('question', kwargs=self.question_ids)

        text_response = self.client.get(reverse('question',
                                                kwargs=self.question_ids))

        assert self.question.body in text_response.content.decode('utf8')
        assert '<Record' in text_response.content.decode('utf8')
        assert question_store_url in text_response.content.decode('utf8')

    def test_transcription_is_enabled(self):
        save_url = reverse('save_response', kwargs=self.question_ids)
        expected_attribute = 'transcribeCallback="%s"' % (save_url)

        text_response = self.client.get(reverse('question',
                                                kwargs=self.question_ids))

        assert expected_attribute in text_response.content.decode('utf8')

    def test_show_numeric_question_during_a_call(self):
        self.question.kind = Question.NUMERIC
        self.question.save()

        numeric_response = self.client.get(reverse('question',
                                                   kwargs=self.question_ids))

        assert 'Gather' in numeric_response.content.decode('utf8')

    def test_show_yesno_question_during_a_call(self):
        self.question.kind = Question.YES_NO
        self.question.save()

        yesno_response = self.client.get(reverse('question',
                                                 kwargs=self.question_ids))

        assert 'Gather' in yesno_response.content.decode('utf8')

    def test_uses_proper_verbs_for_sms(self):
        sms_parameters = {'MessageSid': 'SMS123'}

        text_response = self.client.get(reverse('question',
                                                kwargs=self.question_ids),
                                        sms_parameters)

        assert self.question.body in text_response.content.decode('utf8')
        assert '<Message' in text_response.content.decode('utf8')
        assert '<Record' not in text_response.content.decode('utf8')
        assert '<Say' not in text_response.content.decode('utf8')

    def test_sms_creates_a_web_session(self):
        sms_parameters = {'MessageSid': 'SMS123'}

        self.client.get(reverse('question', kwargs=self.question_ids),
                        sms_parameters)

        assert self.client.session["answering_question_id"] == self.question.id
