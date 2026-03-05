import pytest
from django.test import TestCase
from automated_survey.models import Survey, Question, QuestionResponse
from django.core.exceptions import ValidationError
from django.urls import reverse


class StoreQuestionResponseTest(TestCase):

    def setUp(self):
        self.survey = Survey(title='A testing survey')
        self.survey.save()

    def create_question(self, kind):
        self.question = Question(body='Question one', kind=kind,
                                 survey=self.survey)
        self.question.save()
        self.question_ids = {'survey_id': self.survey.id,
                             'question_id': self.question.id}

    def test_store_response_during_a_call(self):
        self.create_question(Question.TEXT)
        question_store_url = reverse('save_response', kwargs=self.question_ids)

        request_parameters = {
            'CallSid': 'somerandomuniqueid',
            'From': '324238944',
            'RecordingUrl': 'gopher://recording.mp3'
        }

        self.client.post(question_store_url, request_parameters)
        new_response = QuestionResponse.objects.get(question_id=self.question.id)

        assert new_response.call_sid == 'somerandomuniqueid'
        assert new_response.phone_number == '324238944'
        assert new_response.response == 'gopher://recording.mp3'

    def test_store_transcription_update(self):
        self.create_question(Question.TEXT)
        question_store_url = reverse('save_response', kwargs=self.question_ids)

        request_parameters = {
            'CallSid': 'somerandomuniqueid',
            'From': '324238944',
            'RecordingUrl': 'gopher://recording.mp3'
        }

        self.client.post(question_store_url, request_parameters)

        request_parameters['TranscriptionText'] = 'Do you hear me?'
        self.client.post(question_store_url, request_parameters)

        new_response = QuestionResponse.objects.get(question_id=self.question.id)

        assert new_response.call_sid == 'somerandomuniqueid'
        assert new_response.phone_number == '324238944'
        assert new_response.response == 'Do you hear me?'

    def test_store_SMS_response(self):
        self.create_question(Question.TEXT)
        question_store_url = reverse('save_response', kwargs=self.question_ids)

        request_parameters = {
            'MessageSid': 'somerandomuniqueid',
            'From': '324238944',
            'Body': 'I agree with you'
        }

        self.client.post(question_store_url, request_parameters)
        new_response = QuestionResponse.objects.get(question_id=self.question.id)

        assert new_response.call_sid == 'somerandomuniqueid'
        assert new_response.phone_number == '324238944'
        assert new_response.response == 'I agree with you'

    def test_store_response_and_redirect(self):
        self.create_question(Question.NUMERIC)
        question_two = Question(body='Question two', kind=Question.TEXT, survey=self.survey)
        question_two.save()
        question_ids_two = {'survey_id': self.survey.id,
                            'question_id': question_two.id}

        question_store_url_one = reverse('save_response', kwargs=self.question_ids)
        next_question_url = reverse('question', kwargs=question_ids_two)

        request_parameters = {
            'CallSid': 'somerandomuniqueid',
            'From': '324238944',
            'Digits': '4'
        }

        response = self.client.post(question_store_url_one, request_parameters)

        assert '<Redirect method="GET"' in response.content.decode('utf8')
        assert next_question_url in response.content.decode('utf8')

    def test_validate_question_kind(self):
        self.create_question('invalid')
        invalid_question_store_url = reverse('save_response', kwargs=self.question_ids)
        request_parameters = {
            'CallSid': 'somerandomuniqueid',
            'From': '324238944',
            'Digits': '4'
        }
        with pytest.raises(ValidationError):
            self.client.post(invalid_question_store_url, request_parameters)

    def test_last_question_during_a_call(self):
        self.create_question(Question.NUMERIC)
        question_store_url_one = reverse('save_response', kwargs=self.question_ids)
        request_parameters = {
            'CallSid': 'somerandomuniqueid',
            'From': '324238944',
            'Digits': '4'
        }

        response = self.client.post(question_store_url_one, request_parameters)
        response = response.content.decode('utf8')

        assert 'Good-bye' in response
        assert '<Say>' in response
        assert '<Hangup' in response

    def test_last_question_over_sms(self):
        self.create_question(Question.NUMERIC)
        question_store_url_one = reverse('save_response', kwargs=self.question_ids)
        request_parameters = {
            'MessageSid': 'somerandomuniqueid',
            'From': '324238944',
            'Body': '4'
        }

        response = self.client.post(question_store_url_one, request_parameters)
        response = response.content.decode('utf8')

        assert 'Good-bye' in response
        assert '<Message>' in response
        assert 'Redirect' not in response
