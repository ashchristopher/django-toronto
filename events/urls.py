from django.conf.urls import url, patterns

from events.views import EventsListView


urlpatterns = patterns('',
    url(r'^$', EventsListView.as_view(), name='events-list'),
)
