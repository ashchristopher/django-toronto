import factory

from .models import NewsletterSignup


class NewsletterSignupFactory(factory.Factory):
    FACTORY_FOR = NewsletterSignup

    email_address = factory.Sequence(lambda n: 'user.{0}@example.com'.format(n))
    active = True
