from django.test import TestCase
from model_mommy import mommy

from .models import LeadSource, Lead


class LeadSourceTest(TestCase):

    def test_str_name(self):
        # Arrange
        lead_source = mommy.make(
            LeadSource,
            name='Downtown billboard',
            incoming_number='+15555555555')

        # Assert
        self.assertEqual(str(lead_source), 'Downtown billboard - +15555555555')

    def test_str_no_name(self):
        # Arrange
        lead_source = mommy.make(
            LeadSource,
            incoming_number='+15555555555')

        # Assert
        self.assertEqual(str(lead_source), '(not yet named) - +15555555555')

    def test_get_leads_per_source(self):
        # Arrange
        lead_source_1 = mommy.make(
            LeadSource,
            name='Downtown billboard',
            incoming_number='+15555555555')

        mommy.make(Lead,
                   source=lead_source_1,
                   phone_number='+16666666666')

        lead_source_2 = mommy.make(
            LeadSource,
            name='Uptown billboard',
            incoming_number='+17777777777')

        mommy.make(Lead,
                   source=lead_source_2,
                   phone_number='+18888888888')

        mommy.make(Lead,
                   source=lead_source_2,
                   phone_number='+19999999999')

        # Act
        data = LeadSource.objects.get_leads_per_source()

        # Assert
        self.assertEqual(data, [{'name': 'Downtown billboard', 'lead__count': 1}, {
                         'name': 'Uptown billboard', 'lead__count': 2}])


class LeadTest(TestCase):

    def test_str(self):
        # Arrange
        lead_source = mommy.make(
            LeadSource,
            name='Downtown billboard',
            incoming_number='+15555555555')

        lead = mommy.make(
            Lead,
            source=lead_source,
            phone_number='+16666666666')

        # Assert
        self.assertEqual(str(lead), '{0}, {1} at {2}'.format(
            lead.city, lead.state, lead.timestamp))

    def test_get_leads_per_city(self):
        # Arrange
        lead_source = mommy.make(
            LeadSource,
            name='Downtown billboard',
            incoming_number='+15555555555')

        mommy.make(Lead,
                   source=lead_source,
                   phone_number='+16666666666',
                   city='Washington')

        mommy.make(Lead,
                   source=lead_source,
                   phone_number='+17777777777',
                   city='Washington')

        mommy.make(Lead,
                   source=lead_source,
                   phone_number='+18888888888',
                   city='San Francisco')

        # Act
        data = Lead.objects.get_leads_per_city()

        # Assert
        self.assertEqual(data, [{'city': 'San Francisco', 'id__count': 1}, {
                         'city': 'Washington', 'id__count': 2}])
