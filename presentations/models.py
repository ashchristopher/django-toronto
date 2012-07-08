import requests
import tldextract

from django.db import models
from django.utils import simplejson
from django.core.exceptions import ValidationError


class Presentation(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField()
    embed_code = models.TextField()
    owner = models.ForeignKey('auth.User')
    oembed = models.TextField(blank=True, null=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
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

    def get_oembed(self):
        if not getattr(self, 'oembed_dict', None):
            self.oembed_dict = self._oembed_as_dict()
        return self.oembed_dict

    def _oembed_as_dict(self):
        if self.oembed:
            return simplejson.loads(self.oembed)
        return {}
