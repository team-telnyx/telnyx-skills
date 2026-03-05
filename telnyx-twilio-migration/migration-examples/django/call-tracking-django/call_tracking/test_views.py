from django.test import TestCase, Client
from django.urls import reverse
from model_mommy import mommy

import json

from .models import LeadSource, Lead
from .templatetags.phone_number_filter import national_format

# Import Mock if we're running on Python 2
import six

if six.PY3:  # pragma: no cover
    from unittest.mock import patch, Mock, DEFAULT
else:  # pragma: no cover
    from mock import patch, Mock, DEFAULT


class HomePageTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page_extra_context(self):
        # Arrange
        lead_source = mommy.make(LeadSource, incoming_number='+15555555555')

        # Act
        response = self.client.get('/')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn('415', str(response.content))
        self.assertEqual(response.context['lead_sources'][0], lead_source)

    def test_leads_by_source(self):
        # Arrange
        mock_data = {'foo': 'bar'}

        # Act
        with patch('call_tracking.models.LeadSource.objects.get_leads_per_source', return_value=mock_data):
            response = self.client.get('/call-tracking/leads-by-source')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        self.assertEqual(response.content, b'{"foo": "bar"}')

    def test_leads_by_city(self):
        # Arrange
        mock_data = {'foo': 'bar'}

        # Act
        with patch('call_tracking.models.Lead.objects.get_leads_per_city', return_value=mock_data):
            response = self.client.get('/call-tracking/leads-by-city')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        self.assertEqual(response.content, b'{"foo": "bar"}')


class ListNumbersTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_list_numbers_valid_input(self):
        # Arrange
        mock_numbers = ['+15555555555', '+16666666666']

        # Act
        with patch('call_tracking.views.search_phone_numbers', return_value=mock_numbers) as mock:
            response = self.client.post('/call-tracking/list-numbers')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['available_numbers'], mock_numbers)

    def test_list_numbers_none_found(self):
        # Arrange
        mock_numbers = []

        # Act
        with patch('call_tracking.views.search_phone_numbers', return_value=mock_numbers) as mock:
            response = self.client.post(
                '/call-tracking/list-numbers', {'area_code': '703'})

        # Assert
        self.assertRedirects(response, '/')

    def test_list_numbers_invalid_input(self):
        # Act
        response = self.client.post(
            '/call-tracking/list-numbers', {'area_code': '1234'})

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')


class PurchaseNumberTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_purchase_number_valid_input(self):
        # Arrange
        # have to use a real number to get past the form validation
        # mock_telnyx_number now just needs phone_number attribute
        mock_telnyx_number = Mock(phone_number='+14158020512')

        # Act
        with patch('call_tracking.views.purchase_phone_number', return_value=mock_telnyx_number):
            response = self.client.post(
                '/call-tracking/purchase-number', {'phone_number': '+14158020512'})

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertIn('/edit', response.url)

    def test_purchase_number_bad_post_data(self):
        # Arrange
        expected_url = reverse('home')

        # Act
        response = self.client.post(
            '/call-tracking/purchase-number', {'phone_number': 'bad-phone-number'}, follow=True)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], expected_url)
        self.assertIn(
            'bad-phone-number is not a valid phone number. Please search again.', str(response.content))


class ForwardCallTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_forward_call(self):
        # Arrange
        lead_source = mommy.make(
            LeadSource,
            incoming_number='+15555555555',
            forwarding_number='+16666666666')

        # Act
        response = self.client.post(
            '/call-tracking/forward-call',
            {'Called': '+15555555555', 'Caller': '+17777777777', 'CallerCity': 'Washington', 'CallerState': 'DC'})

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn('<Dial>+16666666666</Dial>', str(response.content))

        # Check that a new lead was created
        lead = Lead.objects.get(source=lead_source)
        self.assertEqual(lead.city, 'Washington')
        self.assertEqual(lead.state, 'DC')


class PhoneNumberFilterTest(TestCase):

    def test_phone_number_filter(self):
        # Act
        formatted_number = national_format('+15555555555')

        # Assert
        self.assertEqual(formatted_number, '(555) 555-5555')
