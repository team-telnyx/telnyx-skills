from django.db import models
from django.db.models import Count
from phonenumber_field.modelfields import PhoneNumberField


class LeadSourceManager(models.Manager):
    """A custom manager which adds a 'get_leads_per_source' method"""

    def get_leads_per_source(self):
        """Get the number of leads for each lead source"""
        # Use Django's annotate feature to include the number of leads
        # on each lead source
        queryset = self.all().annotate(Count('lead')).order_by('name')

        # Extract the source names and lead counts and make them a regular list
        data = list(queryset.values('name', 'lead__count'))

        return data


class LeadSource(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        help_text='E.g. "Downtown billboard"')
    incoming_number = PhoneNumberField(
        unique=True,
        help_text='A phone number purchased through Twilio')
    forwarding_number = PhoneNumberField(
        blank=True,
        help_text='People who call this lead source will be connected with this phone number. Must include international prefix - e.g. +1 555 555 55555')

    # Apply our custom manager
    objects = LeadSourceManager()

    def __str__(self):
        if self.name:
            return '{0} - {1}'.format(self.name, self.incoming_number)
        else:
            return '(not yet named) - {0}'.format(self.incoming_number)


class LeadManager(models.Manager):
    """A custom manager which adds a 'get_leads_per_city' method"""

    def get_leads_per_city(self):
        """Get the number of leads for each city"""
        # Use Django's annotate feature to include the number of leads
        # from each distinct city
        queryset = self.all().values('city').annotate(
            Count('id')).order_by('city')

        # Extract the cities and lead counts and make them a regular list
        data = list(queryset.values('city', 'id__count'))

        return data


class Lead(models.Model):
    source = models.ForeignKey(LeadSource, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # A couple examples of fields you could track for each incoming call
    # See https://developers.telnyx.com/docs/voice/texml/texml-reference for more
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    # Apply our custom manager
    objects = LeadManager()

    def __str__(self):
        return '{0}, {1} at {2}'.format(self.city, self.state, self.timestamp)
