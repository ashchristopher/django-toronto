from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pages.views import HomepageView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^presentations/', include('presentations.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^contact-us/', include('contact_us.urls')),
)

urlpatterns += staticfiles_urlpatterns()
