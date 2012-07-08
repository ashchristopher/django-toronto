from datetime import datetime

from django.views.generic import TemplateView
from django.utils.timezone import utc

from events.models import Event
from presentations.models import Presentation


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get(self, request):
        now = datetime.now().replace(tzinfo=utc)

        next_event = Event.objects.filter(date__gte=now).order_by('date')[:1]

        context = {
            'next_event': next_event,
            'latest_presentations': Presentation.objects.all().order_by('-pk')[0:4],
        }

        return self.render_to_response(context)
