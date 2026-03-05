from django.conf import settings
import telnyx

import os

# Uses Telnyx API key
telnyx.api_key = settings.TELNYX_API_KEY


def search_phone_numbers(area_code=None):
    """Queries the Telnyx API to get phone numbers available for purchase"""
    # You can change the country argument to search outside the US
    # area_code is an optional parameter (called national_destination_code in Telnyx)
    filters = {
        "country_code": "US",
        "limit": 10
    }
    if area_code:
        filters["national_destination_code"] = str(area_code)

    numbers = telnyx.AvailablePhoneNumber.list(filter=filters)

    return numbers.data


def purchase_phone_number(phone_number):
    """Purchases a new phone number from the Telnyx API"""
    # Use Number Orders API to purchase numbers
    # Assign to our TeXML Connection for voice handling
    order = telnyx.NumberOrder.create(
        phone_numbers=[{"phone_number": phone_number}],
        connection_id=settings.TELNYX_CONNECTION_ID
    )

    # Return an object with the expected attributes
    # The order contains the number info
    class TelnyxNumberResult:
        def __init__(self, phone_number):
            self.phone_number = phone_number
            self.friendly_name = phone_number

    return TelnyxNumberResult(phone_number)
