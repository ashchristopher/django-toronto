from django.db import models

from .managers import NewsletterManager


SIGNUP_METHODS = (
    ('', '------', ),
    ('website', 'Website', ),
    ('mailchimp', 'MailChimp', )
)


class NewsletterSignup(models.Model):
    email_address = models.EmailField()
    signup_method = models.CharField(max_length=16, choices=SIGNUP_METHODS, default='')
    active = models.BooleanField(default=True, db_index=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = NewsletterManager()

    class Meta:
        unique_together = ('email_address', )

    def __unicode__(self):
        return self.email_address
