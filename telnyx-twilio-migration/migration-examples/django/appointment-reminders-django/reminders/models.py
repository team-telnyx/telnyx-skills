from __future__ import unicode_literals

import redis

from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from django.urls import reverse
from six import python_2_unicode_compatible
from timezone_field import TimeZoneField

import arrow


@python_2_unicode_compatible
class Appointment(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='UTC')

    # Additional fields not visible to users
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Appointment #{0} - {1}'.format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('reminders:view_appointment', args=[str(self.id)])

    def clean(self):
        """Checks that appointments are not scheduled in the past"""

        appointment_time = arrow.get(self.time, self.time_zone.zone)

        if appointment_time < arrow.utcnow():
            raise ValidationError(
                'You cannot schedule an appointment for the past. '
                'Please check your time and time_zone')

    def schedule_reminder(self):
        """Schedule a Dramatiq task to send a reminder for this appointment"""

        # Calculate the correct time to send this reminder
        appointment_time = arrow.get(self.time, self.time_zone.zone)
        reminder_time = appointment_time.shift(minutes=-30)
        now = arrow.now(self.time_zone.zone)
        milli_to_wait = int(
            (reminder_time - now).total_seconds()) * 1000

        # Schedule the Dramatiq task
        from .tasks import send_sms_reminder
        result = send_sms_reminder.send_with_options(
            args=(self.pk,),
            delay=milli_to_wait)

        return result.options['redis_message_id']

    def save(self, *args, **kwargs):
        """Custom save method which also schedules a reminder"""

        # Check if we have scheduled a reminder for this appointment before
        if self.task_id:
            # Revoke that task in case its time has changed
            self.cancel_task()

        # Save our appointment, which populates self.pk,
        # which is used in schedule_reminder
        super(Appointment, self).save(*args, **kwargs)

        # Schedule a new reminder task for this appointment
        self.task_id = self.schedule_reminder()

        # Save our appointment again, with the new task_id
        super(Appointment, self).save(*args, **kwargs)

    def cancel_task(self):
        redis_client = redis.Redis(host=settings.REDIS_LOCAL, port=6379, db=0)
        redis_client.hdel("dramatiq:default.DQ.msgs", self.task_id)
