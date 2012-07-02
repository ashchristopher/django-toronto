from django.contrib import admin

from .models import Presentation


class PresentationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Presentation, PresentationAdmin)
