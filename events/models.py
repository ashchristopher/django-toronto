from django.db import models

from events.managers import EventManager

from icalendar import Calendar, Event as ICSEvent
from datetime import timedelta
from django.utils.timezone import get_current_timezone


class Location(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, default='')
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

    @property
    def ics_string(self):
        cal = Calendar()
        cal.add('prodid', '-//Django Toronto//django-toronto.com//')
        cal.add('version', '2.0')
        event = ICSEvent()
        event.add('summary', ("Django Meetup at %s" % (self.location.name,)))

        timezone = get_current_timezone()
        start_date = self.date.astimezone(timezone)
        event.add('dtstart', start_date)

        next_day = start_date + timedelta(days=1)
        end_date = next_day.replace(hour=0, minute=0, second=0)
        event.add('dtend', end_date)

        event.add('location', self.location.address)
        event.add('url', "http://djangotoronto.com")

        cal.add_component(event)
        return cal.to_ical()
