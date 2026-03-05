from django.urls import reverse
from django.http import HttpResponse
from django.utils.html import escape

from automated_survey.models import Question
from django.views.decorators.http import require_GET


@require_GET
def show_question(request, survey_id, question_id):
    question = Question.objects.get(id=question_id)
    if request.is_sms:
        texml = sms_question(question)
    else:
        texml = voice_question(question)

    request.session['answering_question_id'] = question.id
    return HttpResponse(texml, content_type='application/xml')


def sms_question(question):
    """Generate TeXML Response for SMS survey questions."""
    body_escaped = escape(question.body)
    instructions_escaped = escape(SMS_INSTRUCTIONS[question.kind])

    texml = f'''<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Message>{body_escaped}</Message>
  <Message>{instructions_escaped}</Message>
</Response>'''

    return texml


SMS_INSTRUCTIONS = {
    Question.TEXT: 'Please type your answer',
    Question.YES_NO: 'Please type 1 for yes and 0 for no',
    Question.NUMERIC: 'Please type a number between 1 and 10'
}


def voice_question(question):
    """Generate TeXML Response for Voice survey questions."""
    body_escaped = escape(question.body)
    instructions_escaped = escape(VOICE_INSTRUCTIONS[question.kind])
    action = save_response_url(question)
    action_escaped = escape(action)

    if question.kind == Question.TEXT:
        # For text questions, use Record with transcription
        texml = f'''<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>{body_escaped}</Say>
  <Say>{instructions_escaped}</Say>
  <Record action="{action_escaped}" method="POST" maxLength="6" transcribe="true" transcribeCallback="{action_escaped}"/>
</Response>'''
    else:
        # For YES_NO and NUMERIC questions, use Gather
        texml = f'''<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>{body_escaped}</Say>
  <Say>{instructions_escaped}</Say>
  <Gather action="{action_escaped}" method="POST"/>
</Response>'''

    return texml


VOICE_INSTRUCTIONS = {
    Question.TEXT: 'Please record your answer after the beep and then hit the pound sign',
    Question.YES_NO: 'Please press the one key for yes and the zero key for no and then hit the pound sign',
    Question.NUMERIC: 'Please press a number between 1 and 10 and then hit the pound sign'
}


def save_response_url(question):
    return reverse('save_response',
                   kwargs={'survey_id': question.survey.id,
                           'question_id': question.id})
