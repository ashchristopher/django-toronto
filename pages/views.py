from django.conf import settings
from django.views.generic import TemplateView

from events.mixins import NextEventMixin
from presentations.models import Presentation


class HomepageView(NextEventMixin, TemplateView):
    template_name = 'homepage.html'

    def get(self, request):
        next_event = self._get_next_event()

        context = {
            'next_event': next_event,
            'latest_presentations': Presentation.objects.all().order_by('-pk')[0:4],
            'mailchimp_inline_subscribe_token': settings.MAILCHIMP_INLINE_SUBSCRIBE_TOKEN,
        }

        return self.render_to_response(context)
