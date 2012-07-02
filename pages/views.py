from django.views.generic import TemplateView

from events.models import Event


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get(self, request):

        context = {
            'next_event': Event.objects.all()[0],
        }

        return self.render_to_response(context)
