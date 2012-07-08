from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from events.models import Event


class EventsListView(TemplateView):
    template_name = 'events/list.html'

    def get(self, request):
        page = request.GET.get('page')
        
        all_events = Event.objects.all()
        paginator = Paginator(all_events, 4)

        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            events = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            events = paginator.page(paginator.num_pages)

        context = {
            'events': events,
        }

        return self.render_to_response(context)
