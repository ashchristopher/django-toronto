from django.conf.urls import url, patterns

from events.views import EventsListView, ics


urlpatterns = patterns('',
    url(r'^$', EventsListView.as_view(), name='events-list'),
    url(r'^ics/(?P<event_id>\d+)/$', ics)
)
