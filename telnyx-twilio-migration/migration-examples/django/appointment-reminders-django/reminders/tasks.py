from __future__ import absolute_import

import arrow
import dramatiq
import telnyx

from django.conf import settings

from .models import Appointment


# Uses credentials from the TELNYX_API_KEY environment variable
telnyx.api_key = settings.TELNYX_API_KEY


@dramatiq.actor
def send_sms_reminder(appointment_id):
    """Send a reminder to a phone using Telnyx SMS"""
    # Get our appointment from the database
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        # The appointment we were trying to remind someone about
        # has been deleted, so we don't need to do anything
        return

    appointment_time = arrow.get(appointment.time, appointment.time_zone.zone)
    text = 'Hi {0}. You have an appointment coming up at {1}.'.format(
        appointment.name,
        appointment_time.format('h:mm a')
    )

    telnyx.Message.create(
        text=text,
        to=appointment.phone_number,
        from_=settings.TELNYX_PHONE_NUMBER,
        messaging_profile_id=settings.TELNYX_MESSAGING_PROFILE_ID,
    )
