from django.db import models


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

    def __unicode__(self):
        return "{location} - {date}".format(location=self.location.name, date=self.date)
