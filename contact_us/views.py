from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from contact_us.forms import ContactUsMessageForm
from contact_us.models import ContactUsMessage


class ContactUsView(TemplateView):
    template_name = 'contact_us/index.html'

    def get(self, request):
        form = ContactUsMessageForm()

        context = {
            'form': form,
        }
        
        return self.render_to_response(context)

    def post(self, request):
        request_ip = request.META.get('REMOTE_ADDR')

        model_instance = ContactUsMessage(submitter_ip=request_ip)
        form = ContactUsMessageForm(data=request.POST, instance=model_instance)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

        context = {
            'form': form,
        }

        return self.render_to_response(context)
