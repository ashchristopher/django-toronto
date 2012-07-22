from django import forms

from contact_us.models import ContactUsMessage, BannedIp


class ContactUsMessageForm(forms.ModelForm):
    """ Class to collect `contact us` messages from the user. """

    class Meta:
        model = ContactUsMessage
        fields = ('email_address', 'message', )  # we will only accept the message as user input

    def clean(self):
        cleaned_data = super(ContactUsMessageForm, self).clean()
        ip_data = self.instance.submitter_ip

        if BannedIp.objects.filter(banned_ip=ip_data).exists():
            raise forms.ValidationError("This ip ({ip}) has been banned due to abuse.".format(ip=ip_data))

        return cleaned_data
