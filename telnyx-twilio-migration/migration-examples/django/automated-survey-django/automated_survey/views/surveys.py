from automated_survey.models import Survey, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import escape


@require_GET
def show_survey_results(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    responses_to_render = [response.as_dict() for response in survey.responses]

    template_context = {
        'responses': responses_to_render,
        'survey_title': survey.title
    }

    return render(request, 'results.html', context=template_context)


@csrf_exempt
def show_survey(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    first_question = survey.first_question

    first_question_ids = {
        'survey_id': survey.id,
        'question_id': first_question.id
    }

    first_question_url = reverse('question', kwargs=first_question_ids)
    first_question_url_escaped = escape(first_question_url)

    welcome = 'Hello and thank you for taking the %s survey' % survey.title
    welcome_escaped = escape(welcome)

    if request.is_sms:
        texml = f'''<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Message>{welcome_escaped}</Message>
  <Redirect method="GET">{first_question_url_escaped}</Redirect>
</Response>'''
    else:
        texml = f'''<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>{welcome_escaped}</Say>
  <Redirect method="GET">{first_question_url_escaped}</Redirect>
</Response>'''

    return HttpResponse(texml, content_type='application/xml')


@require_POST
def redirects_telnyx_request_to_proper_endpoint(request):
    """Redirect incoming Telnyx/Twilio requests to the proper survey endpoint."""
    answering_question = request.session.get('answering_question_id')
    if not answering_question:
        first_survey = Survey.objects.first()
        redirect_url = reverse('survey',
                               kwargs={'survey_id': first_survey.id})
    else:
        question = Question.objects.get(id=answering_question)
        redirect_url = reverse('save_response',
                               kwargs={'survey_id': question.survey.id,
                                       'question_id': answering_question})
    return HttpResponseRedirect(redirect_url)


@require_GET
def redirect_to_first_results(request):
    first_survey = Survey.objects.first()
    results_for_first_survey = reverse(
        'survey_results', kwargs={
            'survey_id': first_survey.id})
    return HttpResponseRedirect(results_for_first_survey)
