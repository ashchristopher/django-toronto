from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=120)
    address = models.TextField()

    def __unicode__(self):
        return self.name


class Event(models.Model):
    location = models.ForeignKey('Location')
    date = models.DateTimeField()

    def __unicode__(self):
        return "{location} - {date}".format(location=self.location.name, date=self.date)
