from django.conf import settings
from django.test import TestCase

from .utils import search_phone_numbers, purchase_phone_number

# Import Mock if we're running on Python 2
import six

if six.PY3:  # pragma: no cover
    from unittest.mock import patch, MagicMock
else:  # pragma: no cover
    from mock import patch, MagicMock


class SearchPhoneNumbersTest(TestCase):

    def test_search_phone_numbers(self):
        # Act - Use telnyx.AvailablePhoneNumber.list
        with patch('telnyx.AvailablePhoneNumber.list') as mock:
            mock.return_value = MagicMock(data=[])
            search_phone_numbers()

        # Assert
        self.assertTrue(mock.called)
        mock.assert_called_with(filter={'country_code': 'US', 'limit': 10})

    def test_search_phone_numbers_with_area_code(self):
        # Act - Use telnyx.AvailablePhoneNumber.list
        with patch('telnyx.AvailablePhoneNumber.list') as mock:
            mock.return_value = MagicMock(data=[])
            search_phone_numbers(415)

        # Assert
        self.assertTrue(mock.called)
        mock.assert_called_with(filter={'country_code': 'US', 'limit': 10, 'national_destination_code': '415'})


class PurchasePhoneNumberTest(TestCase):

    def test_purchase_phone_number(self):
        # Act - Use telnyx.NumberOrder.create
        with patch('telnyx.NumberOrder.create') as mock:
            purchase_phone_number(phone_number='+15555555555')

        # Assert
        self.assertTrue(mock.called)
        mock.assert_called_with(
            phone_numbers=[{'phone_number': '+15555555555'}],
            connection_id=settings.TELNYX_CONNECTION_ID)
