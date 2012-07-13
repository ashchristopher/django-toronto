#!/usr/bin/env python
#-*- coding: utf-8 -*-

from datetime import timedelta
import urllib

from django import template
from django.utils.timezone import get_current_timezone

register = template.Library()


@register.simple_tag
def create_google_calendar_url(event):
    """
    Generates a Google Calendar creation link based on event details.

    See http://support.google.com/calendar/bin/answer.py?hl=en&answer=1186917
    and http://support.google.com/calendar/bin/answer.py?hl=en&answer=2476685
    for information on how to generate a link and what each field means.

    """

    location = event.location
    calendar_base_url = 'http://www.google.com/calendar/event?'
    timezone = get_current_timezone()
    strftime_format = '%Y%m%dT%H%M00'

    start_date = event.date.astimezone(timezone)
    # There is no end date, but pretend the end date is 12am that night
    # or 00:00:00am the next day
    next_day = start_date + timedelta(days=1)
    end_date = next_day.replace(hour=0, minute=0, second=0)

    data = {
        # action and trp are defaults for creating calendar events
        'action': 'TEMPLATE',
        'trp': 'true',  # show as busy
        # Event-specific values
        'dates': '{start}/{end}'.format(
            start=start_date.strftime(strftime_format),
            end=end_date.strftime(strftime_format)
        ),
        'details': '',
        'location': location.address,
        'sprop': 'http://djangotoronto.com',
        'sprop': 'name:Django Toronto',
        'text': 'Django Toronto Meetup - {name}'.format(name=location.name)
    }

    full_url = '{base_url}{querystring}'.format(
        base_url=calendar_base_url,
        querystring=urllib.urlencode(data)
    )

    return full_url
