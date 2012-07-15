from django.db import models

from events.managers import EventManager


class Location(models.Model):
    name = models.CharField(max_length=120)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return self.name


class Event(models.Model):
    location = models.ForeignKey('Location')
    presentations = models.ManyToManyField('presentations.Presentation', blank=True, null=True)
    date = models.DateTimeField(db_index=True)
    plancast_id = models.CharField(help_text='Base 36 code which can be found in the plancast url: http://plancast.com/p/:plancast_id/django-toronto-meetup', max_length=8, blank=True, null=True)

    objects = EventManager()

    def __unicode__(self):
        return "{location} - {date}".format(location=self.location.name, date=self.date)
