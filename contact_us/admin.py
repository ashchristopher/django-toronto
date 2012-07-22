from django.contrib import admin

from contact_us.models import ContactUsMessage, BannedIp


class ContactUsMessageAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'submitter_ip', 'date_added', )


class BannedIpAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContactUsMessage, ContactUsMessageAdmin)
admin.site.register(BannedIp, BannedIpAdmin)
