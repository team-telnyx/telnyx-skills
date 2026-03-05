from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.utils.html import escape

from automated_survey.models import QuestionResponse, Question


@require_POST
def save_response(request, survey_id, question_id):
    question = Question.objects.get(id=question_id)

    save_response_from_request(request, question)

    next_question = question.next()
    if not next_question:
        return goodbye(request)
    else:
        return next_question_redirect(next_question.id, survey_id)


def next_question_redirect(question_id, survey_id):
    parameters = {'survey_id': survey_id, 'question_id': question_id}
    question_url = reverse('question', kwargs=parameters)
    question_url_escaped = escape(question_url)

    texml = f'''<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Redirect method="GET">{question_url_escaped}</Redirect>
</Response>'''

    return HttpResponse(texml, content_type='application/xml')


def goodbye(request):
    goodbye_messages = ['That was the last question',
                        'Thank you for taking this survey',
                        'Good-bye']

    if request.is_sms:
        # SMS response with multiple messages
        messages_xml = '\n  '.join([f'<Message>{escape(msg)}</Message>' for msg in goodbye_messages])
        texml = f'''<?xml version="1.0" encoding="UTF-8"?>
<Response>
  {messages_xml}
</Response>'''
    else:
        # Voice response with say and hangup
        say_xml = '\n  '.join([f'<Say>{escape(msg)}</Say>' for msg in goodbye_messages])
        texml = f'''<?xml version="1.0" encoding="UTF-8"?>
<Response>
  {say_xml}
  <Hangup/>
</Response>'''

    return HttpResponse(texml, content_type='application/xml')


def save_response_from_request(request, question):
    # Support both Twilio form-encoded (POST) and Telnyx JSON webhook formats
    if hasattr(request, 'is_sms') and request.is_sms:
        # SMS uses MessageSid, Voice uses CallSid
        session_id = request.POST.get('MessageSid') or request.POST.get('CallSid')
    else:
        # For Telnyx JSON webhooks, these would be in the JSON payload
        # For now, maintain backward compatibility with form-encoded
        session_id = request.POST.get('CallSid') or request.POST.get('MessageSid')

    request_body = _extract_request_body(request, question.kind)
    phone_number = request.POST.get('From')

    # Handle Telnyx payload format if present
    if not phone_number and request.content_type == 'application/json':
        import json
        try:
            data = json.loads(request.body)
            payload = data.get('data', {}).get('payload', {})
            session_id = payload.get('id') or session_id
            if payload.get('from'):
                phone_number = payload['from'].get('phone_number')
            else:
                phone_number = payload.get('from')
        except (json.JSONDecodeError, AttributeError):
            pass

    response = QuestionResponse.objects.filter(question_id=question.id,
                                               call_sid=session_id).first()

    if not response:
        QuestionResponse(call_sid=session_id,
                         phone_number=phone_number,
                         response=request_body,
                         question=question).save()
    else:
        response.response = request_body
        response.save()


def _extract_request_body(request, question_kind):
    Question.validate_kind(question_kind)

    # Support both Twilio form-encoded and Telnyx JSON formats
    if request.content_type == 'application/json':
        import json
        try:
            data = json.loads(request.body)
            payload = data.get('data', {}).get('payload', {})

            if hasattr(request, 'is_sms') and request.is_sms:
                return payload.get('text', '')
            elif question_kind in [Question.YES_NO, Question.NUMERIC]:
                return payload.get('digits', '')
            elif 'transcription' in payload:
                return payload['transcription']
            else:
                return payload.get('recording_url', '')
        except (json.JSONDecodeError, AttributeError):
            pass

    # Fall back to form-encoded (Twilio/Telnyx TeXML compatible)
    if hasattr(request, 'is_sms') and request.is_sms:
        key = 'Body'
    elif question_kind in [Question.YES_NO, Question.NUMERIC]:
        key = 'Digits'
    elif 'TranscriptionText' in request.POST:
        key = 'TranscriptionText'
    else:
        key = 'RecordingUrl'

    return request.POST.get(key)
