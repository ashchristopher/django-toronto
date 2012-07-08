from django.views.generic import TemplateView

from events.models import Event
from presentations.models import Presentation


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get(self, request):

        context = {
            'next_event': Event.objects.all()[0],
            'latest_presentations': Presentation.objects.all().order_by('-pk')[0:4],
        }

        return self.render_to_response(context)
