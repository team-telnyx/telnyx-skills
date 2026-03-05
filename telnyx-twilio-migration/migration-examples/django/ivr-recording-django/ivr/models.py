from django.db import models


# Create your models here.
class Recording(models.Model):
    caller_number = models.CharField(max_length=20)
    transcription = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return (
            f'Caller: {self.caller_number}; '
            f'Transcription: {self.transcription}; '
            f'url: {self.url}'
        )


class Agent(models.Model):
    recordings = models.ManyToManyField(Recording, blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @property
    def all_recordings(self):
        return self.recordings.all()
