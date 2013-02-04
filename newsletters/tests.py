from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from .factories import NewsletterSignupFactory
from .models import NewsletterSignup


class NewsletterManagerSignupTestCase(TestCase):
    
    def test_get_subscribers_none(self):
        """
        Tests that when there are no newsletter signups, make sure subscribers list is empty.
        """
        subscribers = NewsletterSignup.objects.subscribers()

        self.assertEqual(subscribers.count(), 0)

    def test_get_subscribers_active(self):
        """
        Tests that when we add newsletter subscriptions, they are returned by the model managers
        subscribers() call.
        """
        for i in xrange(3):
            NewsletterSignupFactory.create()

        subscribers = NewsletterSignup.objects.subscribers()
        self.assertEqual(subscribers.count(), 3)

    def test_subscribers_inactive(self):
        """
        Tests that inactive NewsletterSignups are not returned when requesting subscribers
        from the manager.
        """
        for i in xrange(3):
            NewsletterSignupFactory.create(active=False)

        subscribers = NewsletterSignup.objects.subscribers()
        self.assertEqual(subscribers.count(), 0)

    def test_subscribers_list(self):
        """
        Tests that we can get a list of email addresses.
        """
        test_emails = []
        for i in xrange(3):
            test_email = NewsletterSignupFactory.create(active=True)
            test_emails.append(test_email.email_address)

        self.assertEqual(
            set(NewsletterSignup.objects.subscribers_list()),
            set(test_emails)
        )


class NewsletterSignupIntegrationTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_sign_up_for_newsletter(self):
        """
        Tests that a user can signup for a newsletter.
        """
        url = reverse('newsletter-signup')
        response = self.client.post(url, {'email_address': u'foo@example.com', })

        self.assertEqual(response.status_code, 302)  # redirect back to the home page
        self.assertEqual(NewsletterSignup.objects.subscribers().count(), 1)
        self.assertTrue(u'foo@example.com' in NewsletterSignup.objects.subscribers_list())
