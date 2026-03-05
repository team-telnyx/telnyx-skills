"""
Tests for IVR views (Telnyx TeXML version)
"""
from django.test import TestCase
from django.urls import reverse

from .models import Agent, Recording


class IVRViewsTest(TestCase):
    """Test cases for IVR views with Telnyx TeXML responses."""

    def test_index(self):
        """Test index page returns 200."""
        response = self.client.get(reverse('ivr:index'))
        self.assertEqual(response.status_code, 200)

    def test_agents(self):
        """Test agents page returns 200."""
        response = self.client.get(reverse('ivr:agents'))
        self.assertEqual(response.status_code, 200)

    def test_welcome(self):
        """Test welcome endpoint returns correct TeXML."""
        response = self.client.post(reverse('ivr:welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        # Parse the XML response
        expected_content = (
            b'<?xml version="1.0" encoding="UTF-8"?>'
            b'<Response><Gather action="/ivr/menu/" numDigits="1">'
            b'<Play loop="3">https://can-tasty-8188.twil.io/assets/et-phone.mp3</Play>'
            b'</Gather></Response>'
        )
        self.assertEqual(response.content, expected_content)

    def test_menu_instructions_option(self):
        """Test menu option 1 returns instructions."""
        response = self.client.post(reverse('ivr:menu'), {'Digits': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        # Check for expected content in the TeXML
        content = response.content.decode('utf-8')
        self.assertIn('<Response>', content)
        self.assertIn('To get to your extraction point', content)
        self.assertIn('Polly.Amy-Neural', content)
        self.assertIn('en-GB', content)
        self.assertIn('<Hangup />', content)

    def test_menu_planets_option(self):
        """Test menu option 2 returns planets menu."""
        response = self.client.post(reverse('ivr:menu'), {'Digits': '2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        content = response.content.decode('utf-8')
        self.assertIn('<Response>', content)
        self.assertIn('planet Broh doe As O G', content)
        self.assertIn('action="/ivr/agent/connect"', content)

    def test_menu_invalid_option(self):
        """Test invalid menu option redirects to welcome."""
        response = self.client.post(reverse('ivr:menu'), {'Digits': '6'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        content = response.content.decode('utf-8')
        self.assertIn('<Redirect>', content)
        self.assertIn('/ivr/welcome/', content)

    def test_agent_connect_valid(self):
        """Test connecting to valid agent."""
        agent = Agent.objects.create(name='Brodo', phone_number='1234567890')
        response = self.client.post(reverse('ivr:agent_connect'), {'Digits': '2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        content = response.content.decode('utf-8')
        self.assertIn('<Response>', content)
        self.assertIn('You\'ll be connected shortly', content)
        self.assertIn('callerId="1234567890"', content)
        self.assertIn('<Number', content)
        self.assertIn('1234567890</Number>', content)
        self.assertIn('/ivr/agent/screencall', content)

    def test_agent_connect_invalid(self):
        """Test connecting with invalid digits redirects to welcome."""
        response = self.client.post(reverse('ivr:agent_connect'), {'Digits': '8'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        content = response.content.decode('utf-8')
        self.assertIn('<Redirect>', content)
        self.assertIn('/ivr/welcome/', content)

    def test_agent_call_completed(self):
        """Test agent call when status is completed returns empty response."""
        response = self.client.post(
            reverse('ivr:agents_call'), {'CallStatus': 'completed'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'')

    def test_agent_call_not_completed(self):
        """Test agent call when not completed returns recording TeXML."""
        response = self.client.post(
            f"{reverse('ivr:agents_call')}?agentId=1", {'CallStatus': 'ongoing'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        content = response.content.decode('utf-8')
        self.assertIn('<Response>', content)
        self.assertIn('Please leave a message after the beep', content)
        self.assertIn('<Record', content)
        self.assertIn('channels="single"', content)

    def test_hangup(self):
        """Test hangup endpoint."""
        response = self.client.post(reverse('ivr:hangup'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        content = response.content.decode('utf-8')
        self.assertIn('Thanks for your message. Goodbye', content)
        self.assertIn('<Hangup />', content)

    def test_screencall(self):
        """Test screencall endpoint."""
        response = self.client.post(
            reverse('ivr:agents_screencall'), {'From': '1234567890'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        content = response.content.decode('utf-8')
        self.assertIn('<Response>', content)
        self.assertIn('Gather', content)
        self.assertIn('1 2 3 4 5 6 7 8 9 0', content)
        self.assertIn('Press any key to accept', content)

    def test_connect_message(self):
        """Test connect message endpoint."""
        response = self.client.post(reverse('ivr:agents_connect_message'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')

        content = response.content.decode('utf-8')
        self.assertIn('<Response>', content)
        self.assertIn('Connecting you to the extraterrestrial in distress', content)

    def test_create_recordings(self):
        """Test creating a recording via callback."""
        agent = Agent.objects.create(name='Brodo', phone_number='222222222')
        response = self.client.post(
            f"{reverse('ivr:recordings')}?agentId={agent.id}",
            {
                'From': '1234567890',
                'TranscriptionText': 'Sample',
                'RecordingUrl': '/test/url',
            },
        )
        self.assertEqual(response.status_code, 201)
        recordings_count = Recording.objects.count()
        self.assertEqual(recordings_count, 1)

    def test_recordings_agent_not_found(self):
        """Test recording callback with invalid agent ID."""
        response = self.client.post(
            f"{reverse('ivr:recordings')}?agentId=999",
            {
                'From': '1234567890',
                'TranscriptionText': 'Sample',
                'RecordingUrl': '/test/url',
            },
        )
        self.assertEqual(response.status_code, 500)
