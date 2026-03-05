from django.conf.urls import url
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from automated_survey.views.surveys import redirects_telnyx_request_to_proper_endpoint
from automated_survey.views.surveys import redirect_to_first_results
from automated_survey.views.questions import show_question
from automated_survey.views.surveys import show_survey, show_survey_results
from automated_survey.views.question_responses import save_response

urlpatterns = [
    re_path(r'^$', redirect_to_first_results, name='app_root'),

    re_path(r'^survey/(?P<survey_id>\d+)/question/(?P<question_id>\d+)$',
        show_question,
        name='question'),

    re_path(r'^survey/(?P<survey_id>\d+)$',
        show_survey,
        name='survey'),

    re_path(r'^first-survey/',
        csrf_exempt(redirects_telnyx_request_to_proper_endpoint),
        name='first_survey'),

    re_path(r'^survey/(?P<survey_id>\d+)/results$',
        show_survey_results,
        name='survey_results'),

    re_path(r'^survey/(?P<survey_id>\d+)/question/(?P<question_id>\d+)/question_response$',
        csrf_exempt(save_response),
        name='save_response')
]
