from django.core.exceptions import ValidationError
from django.test import TestCase
from model_mommy import mommy

from reminders.models import Appointment
from reminders.tasks import send_sms_reminder

import arrow

# Import Mock if we're running on Python 2
import six

if six.PY3:
    from unittest.mock import patch
else:
    from mock import patch


class AppointmentTest(TestCase):

    @patch('reminders.models.Appointment.schedule_reminder', return_value='fake-id')
    def test_str(self, _):
        # Arrange
        appointment = mommy.make(Appointment, name='John')

        # Assert
        self.assertEqual(
            str(appointment),
            'Appointment #{0} - {1}'.format(appointment.pk, appointment.name))

    @patch('reminders.models.Appointment.schedule_reminder', return_value='fake-id')
    def test_get_absolute_url(self, _):
        # Arrange
        appointment = mommy.make(Appointment)

        # Assert
        self.assertEqual(
            appointment.get_absolute_url(),
            '/{0}'.format(appointment.pk))

    @patch('reminders.models.Appointment.schedule_reminder', return_value='fake-id')
    def test_clean_invalid_appointment(self, _):
        # Arrange
        time_in_past = arrow.utcnow().shift(minutes=-10)
        appointment = mommy.make(Appointment, time=time_in_past.datetime)

        # Assert
        with self.assertRaises(ValidationError):
            appointment.clean()

    @patch('reminders.models.Appointment.schedule_reminder', return_value='fake-id')
    def test_clean_valid_appointment(self, _):
        # Arrange
        time_in_future = arrow.utcnow().shift(minutes=+10)
        appointment = mommy.make(Appointment, time=time_in_future.datetime)

        # Assert
        try:
            appointment.clean()
        except ValidationError:
            self.fail(
                'appointment with time in the past raised ValidationError')

    def test_schedule_reminder(self):
        # Arrange
        with patch('reminders.models.Appointment.schedule_reminder', return_value='fake-id'):
            appointment = mommy.make(Appointment)

        # Act
        with patch.object(send_sms_reminder, 'send_with_options') as mock:
            appointment.schedule_reminder()

        # Assert
        self.assertTrue(mock.called)

    @patch('reminders.models.Appointment.schedule_reminder', return_value='fake-id')
    def test_save_initial_creation(self, mock):
        # Act
        appointment = mommy.make(Appointment)

        # Assert
        self.assertTrue(mock.called)
        self.assertEqual(appointment.task_id, 'fake-id')

    @patch('reminders.models.Appointment.schedule_reminder', return_value='fake-id')
    def test_save_revoke_existing_task(self, _):
        # Arrange
        appointment = mommy.make(Appointment)

        # Act
        with patch('reminders.models.Appointment.cancel_task') as mock:
            appointment.save()

        # Assert
        self.assertTrue(mock.called)


class SendReminderTest(TestCase):
    @patch('reminders.models.Appointment.schedule_reminder', return_value='fake-id')
    def test_create_message(self, _):
        # Arrange
        appointment = mommy.make(Appointment)

        # Act
        with patch('telnyx.Message.create') as mock:
            send_sms_reminder(appointment.pk)

        # Assert
        self.assertTrue(mock.called)

    @patch('reminders.models.Appointment.schedule_reminder', return_value='fake-id')
    def test_deleted_appointment(self, _):
        # Arrange
        appointment = mommy.make(Appointment)
        appointment.delete()

        # Act
        with patch('telnyx.Message.create') as mock:
            send_sms_reminder(appointment.pk)

        # Assert
        self.assertFalse(mock.called)
