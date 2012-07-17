from django.views.generic import TemplateView

from contact_us.forms import ContactUsMessageForm


class ContactUsView(TemplateView):
    template_name = 'contact_us/index.html'

    def get(self, request):
        form = ContactUsMessageForm()

        context = {
            'form': form,
        }
        
        return self.render_to_response(context)
