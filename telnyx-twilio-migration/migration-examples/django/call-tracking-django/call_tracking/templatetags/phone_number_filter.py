from django import template

import phonenumbers

register = template.Library()


@register.filter
def national_format(value):
    """Displays a phone number in an appropriate national format"""

    # Since this is a template filter, we will just pass through
    # the original value if we encounter any error
    try:
        number = phonenumbers.parse(value)
        formatted_number = phonenumbers.format_number(
            number, phonenumbers.PhoneNumberFormat.NATIONAL)
    except Exception:
        return value

    return formatted_number
