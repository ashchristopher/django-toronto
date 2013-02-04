from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy

from .forms import NewsletterSignupModelForm


class NewsletterSignupView(FormView):
    template_name = 'newsletters/signup.html'
    form_class = NewsletterSignupModelForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.signup_method = 'website'
        instance.save()
        return super(NewsletterSignupView, self).form_valid(form)
