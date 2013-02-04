from django import forms

from .models import NewsletterSignup


class NewsletterSignupModelForm(forms.ModelForm):
    """
    Form for processing newsletter signups.
    """

    class Meta:
        model = NewsletterSignup
        fields = ('email_address', )
