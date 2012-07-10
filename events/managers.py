from datetime import datetime

from django.db import models
from django.utils.timezone import utc


class EventManager(models.Manager):

    def next_event(self):
        now = datetime.now().replace(tzinfo=utc)
        next_events_qs = self.filter(date__gte=now).select_related('location').order_by('date')[:1]

        if next_events_qs:
            next_event = next_events_qs[0]
            return next_event
        
        raise self.model.DoesNotExist
