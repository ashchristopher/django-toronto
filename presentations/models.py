import requests
import tldextract

from django.db import models
from django.utils import simplejson
from django.core.exceptions import ValidationError


class Presentation(models.Model):
    url = models.URLField()
    owner = models.ForeignKey('auth.User')
    oembed = models.TextField(blank=True, null=True)
    
    def clean(self):
        result = tldextract.extract(self.url)

        if not result.domain == 'speakerdeck':
            raise ValidationError('We only accept presentations from SpeakerDeck.')

    def save(self, *args, **kwargs):
        self.full_clean()
        r = requests.get('https://speakerdeck.com/oembed.json?url={0}'.format(self.url))
        if r.status_code == 200:
            self.oembed = r.content
        super(Presentation, self).save(*args, **kwargs)

    def oembed_as_dict(self):
        if self.oembed:
            return simplejson.loads(self.oembed)
        return {}
