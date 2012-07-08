from django.conf.urls import url, patterns

from presentations.views import PresentationsListView

urlpatterns = patterns('',
    url(r'^$', PresentationsListView.as_view(), name='presentations-list'),
)
