from django.contrib import admin

from .models import Presentation


class PresentationAdmin(admin.ModelAdmin):
    fields = ('url', 'owner')


admin.site.register(Presentation, PresentationAdmin)
