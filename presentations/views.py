from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from presentations.models import Presentation


class PresentationsListView(TemplateView):
    template_name = 'presentations/list.html'

    def get(self, request):
        page = request.GET.get('page')
        all_presentations = Presentation.objects.all().order_by('-id')
        paginator = Paginator(all_presentations, 4)

        try:
            presentations = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            presentations = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            presentations = paginator.page(paginator.num_pages)

        context = {
            'presentations': presentations,
            'paginator': paginator,
        }

        return self.render_to_response(context)
