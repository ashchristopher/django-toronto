from django.db import models


class NewsletterManager(models.Manager):

    def subscribers(self):
        return self.filter(active=True)

    def subscribers_list(self):
        return self.subscribers().values_list('email_address', flat=True)
