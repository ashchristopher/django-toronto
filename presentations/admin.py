from django.contrib import admin

from .models import Presentation


class PresentationAdmin(admin.ModelAdmin):
    exclude = ('oembed',)


admin.site.register(Presentation, PresentationAdmin)
