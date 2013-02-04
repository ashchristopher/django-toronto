from django.contrib import admin

from .models import NewsletterSignup


class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'active', 'date_added', 'date_modified', )

admin.site.register(NewsletterSignup, NewsletterSignupAdmin)
