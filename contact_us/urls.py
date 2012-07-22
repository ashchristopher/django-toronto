from django.conf.urls import url, patterns

from contact_us.views import ContactUsView, ContactUsViewComplete

urlpatterns = patterns('',
    url(r'^$', ContactUsView.as_view(), name='contact_us'),
    url(r'^complete/$', ContactUsViewComplete.as_view(), name='contact_us_complete'),
)
