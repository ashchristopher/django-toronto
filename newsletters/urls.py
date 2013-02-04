from django.conf.urls import patterns, url

from .views import NewsletterSignupView


urlpatterns = patterns('',
    url(r'^$', NewsletterSignupView.as_view(), name='newsletter-signup'),

)
