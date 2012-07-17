from django import forms

from contact_us.models import ContactUsMessage


class ContactUsMessageForm(forms.ModelForm):
    """ Class to collect `contact us` messages from the user. """

    class Meta:
        model = ContactUsMessage
        fields = ('email_address', 'message', )  # we will only accept the message as user input
