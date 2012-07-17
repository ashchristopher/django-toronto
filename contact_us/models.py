from django.db import models


class ContactUsMessage(models.Model):
    submitter_ip = models.IPAddressField()
    email_address = models.EmailField()
    message = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Message from {email}".format(email=self.email_address)


class BannedIp(models.Model):
    banned_ip = models.IPAddressField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Banned {ip}".format(ip=self.banned_ip)
