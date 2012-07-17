from django.conf.urls import url, patterns

from contact_us.views import ContactUsView

urlpatterns = patterns('',
    url(r'^$', ContactUsView.as_view(), name='contact_us'),
)
