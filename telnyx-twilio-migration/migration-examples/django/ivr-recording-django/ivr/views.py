"""
IVR Views - Telnyx TeXML version (migrated from Twilio TwiML)

This module handles IVR (Interactive Voice Response) call flows using Telnyx TeXML,
which is compatible with Twilio TwiML.
"""
import xml.etree.ElementTree as ET
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import Agent, Recording


def index(request):
    """Render the main index page."""
    context = {'title': 'Sample IVR Recordings'}
    return render(request, 'ivr/index.html', context)


def agents(request):
    """Render the agents page with recordings."""
    agents = Agent.objects.order_by('name')
    context = {'agents': agents}
    return render(request, 'ivr/agents.html', context)


class TeXMLResponse(HttpResponse):
    """Helper class for TeXML responses with proper content type."""
    def __init__(self, content='', *args, **kwargs):
        kwargs['content_type'] = 'application/xml'
        super().__init__(content, *args, **kwargs)


def _texml_response_from_element(root_element):
    """Convert an XML element to a TeXML response string."""
    xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>'
    xml_string = ET.tostring(root_element, encoding='unicode')
    return f'{xml_declaration}{xml_string}'


@csrf_exempt
def welcome(request):
    """Welcome endpoint - plays greeting and collects menu selection."""
    response = ET.Element('Response')
    gather = ET.SubElement(response, 'Gather', {
        'action': reverse('ivr:menu'),
        'numDigits': '1'
    })
    play = ET.SubElement(gather, 'Play', {'loop': '3'})
    play.text = 'https://can-tasty-8188.twil.io/assets/et-phone.mp3'

    return TeXMLResponse(_texml_response_from_element(response))


# MAIN MENU


@csrf_exempt
def menu(request):
    """Handle menu selection from welcome."""
    selected_option = request.POST.get('Digits', '')
    options = {
        '1': return_instructions,
        '2': planets,
    }
    action = options.get(selected_option, redirect_welcome)
    return TeXMLResponse(action())


def return_instructions():
    """Return instructions for extraction point."""
    response = ET.Element('Response')

    say1 = ET.SubElement(response, 'Say', {
        'voice': 'Polly.Amy-Neural',
        'language': 'en-GB'
    })
    say1.text = (
        "To get to your extraction point, get on your bike and go down "
        "the street. Then Left down an alley. Avoid the police cars. "
        "Turn left into an unfinished housing development. Fly over "
        "the roadblock. Go passed the moon. Soon after you will see "
        "your mother ship."
    )

    say2 = ET.SubElement(response, 'Say')
    say2.text = (
        "Thank you for calling the ET Phone Home Service - the "
        "adventurous alien's first choice in intergalactic travel"
    )

    ET.SubElement(response, 'Hangup')
    return _texml_response_from_element(response)


def planets():
    """Present planet selection menu."""
    response = ET.Element('Response')
    gather = ET.SubElement(response, 'Gather', {
        'action': reverse('ivr:agent_connect'),
        'numDigits': '1'
    })
    say = ET.SubElement(gather, 'Say', {
        'voice': 'Polly.Amy-Neural',
        'language': 'en-GB',
        'loop': '3'
    })
    say.text = (
        "To call the planet Broh doe As O G, press 2. To call the "
        "planet DuhGo bah, press 3. To call an oober asteroid to your "
        "location, press 4. To go back to the main menu, press "
        "the star key "
    )

    return _texml_response_from_element(response)


def redirect_welcome():
    """Redirect back to welcome."""
    response = ET.Element('Response')
    ET.SubElement(response, 'Redirect').text = reverse('ivr:welcome')
    return _texml_response_from_element(response)


# AGENTS


@csrf_exempt
def agent_connect(request):
    """Connect caller to selected agent."""
    selected_option = request.POST.get('Digits', '')
    agents = {
        '2': 'Brodo',
        '3': 'Dagobah',
        '4': 'Oober',
    }
    selected_agent = agents.get(selected_option)

    if not selected_agent:
        # Bad user input
        return TeXMLResponse(redirect_welcome())

    try:
        agent = Agent.objects.get(name=selected_agent)
    except Agent.DoesNotExist:
        return TeXMLResponse(redirect_welcome())

    response = ET.Element('Response')
    say = ET.SubElement(response, 'Say', {
        'voice': 'Polly.Amy-Neural',
        'language': 'en-GB'
    })
    say.text = "You'll be connected shortly to your planet."

    # Create Dial element with action and callerId attributes
    dial = ET.SubElement(response, 'Dial', {
        'action': f"{reverse('ivr:agents_call')}?agentId={agent.id}",
        'callerId': agent.phone_number,
    })

    # Add Number child with url attribute
    number = ET.SubElement(dial, 'Number', {
        'url': reverse('ivr:agents_screencall')
    })
    number.text = agent.phone_number

    return TeXMLResponse(_texml_response_from_element(response))


@csrf_exempt
def agent_call(request):
    """Handle agent call completion or voicemail recording."""
    if request.POST.get('CallStatus') == 'completed':
        return HttpResponse('')

    response = ET.Element('Response')
    say = ET.SubElement(response, 'Say', {
        'voice': 'Polly.Amy-Neural',
        'language': 'en-GB'
    })
    say.text = (
        'It appears that no agent is available. Please leave a message after the beep'
    )

    # Get agentId from query parameters
    agent_id = request.GET.get('agentId', '')

    ET.SubElement(response, 'Record', {
        'maxLength': '20',
        'action': reverse('ivr:hangup'),
        'transcribeCallback': f"{reverse('ivr:recordings')}?agentId={agent_id}",
        'channels': 'single',  # Match Twilio behavior - use single channel
    })

    return TeXMLResponse(_texml_response_from_element(response))


@csrf_exempt
def hangup(request):
    """Handle hangup after recording."""
    response = ET.Element('Response')
    say = ET.SubElement(response, 'Say', {
        'voice': 'Polly.Amy-Neural',
        'language': 'en-GB'
    })
    say.text = 'Thanks for your message. Goodbye'
    ET.SubElement(response, 'Hangup')

    return TeXMLResponse(_texml_response_from_element(response))


@csrf_exempt
def screencall(request):
    """Screen incoming call before connecting to agent."""
    response = ET.Element('Response')
    gather = ET.SubElement(response, 'Gather', {
        'action': reverse('ivr:agents_connect_message'),
    })

    phone_number = request.POST.get('From', '')
    spelled_phone_number = ' '.join(char for char in phone_number)

    say1 = ET.SubElement(gather, 'Say')
    say1.text = spelled_phone_number

    say2 = ET.SubElement(gather, 'Say')
    say2.text = 'Press any key to accept'

    say3 = ET.SubElement(response, 'Say')
    say3.text = 'Sorry. Did not get your response'

    ET.SubElement(response, 'Hangup')

    return TeXMLResponse(_texml_response_from_element(response))


@csrf_exempt
def connect_message(request):
    """Connect message after screening."""
    response = ET.Element('Response')
    say = ET.SubElement(response, 'Say')
    say.text = 'Connecting you to the extraterrestrial in distress'

    return TeXMLResponse(_texml_response_from_element(response))


# RECORDINGS


@csrf_exempt
def recordings(request):
    """Handle recording callback and save transcription."""
    agent_id = request.GET.get('agentId')

    try:
        agent = Agent.objects.get(pk=agent_id)
    except (Agent.DoesNotExist, TypeError, ValueError):
        return HttpResponseServerError('Agent not found')

    # Note: TeXML sends form-encoded data for transcription callbacks
    # similar to Twilio, so we use request.POST
    try:
        # Check for Telnyx webhook format differences
        # Telnyx uses nested data structure in Call Control
        # TeXML uses form-encoded similar to Twilio
        caller_number = request.POST.get('From', request.POST.get('from', ''))
        transcription = request.POST.get('TranscriptionText', request.POST.get('transcription_text', ''))
        recording_url = request.POST.get('RecordingUrl', request.POST.get('recording_url', ''))

        recording = Recording.objects.create(
            caller_number=caller_number,
            transcription=transcription,
            url=recording_url,
        )
        agent.recordings.add(recording)
    except Exception:  # noqa
        return HttpResponseServerError('Could not create a recording')
    else:
        return HttpResponse('Recording created', status=201)
