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
    presentations = models.ManyToManyField('presentations.Presentation')
    date = models.DateTimeField(db_index=True)

    objects = EventManager()

    def __unicode__(self):
        return "{location} - {date}".format(location=self.location.name, date=self.date)
