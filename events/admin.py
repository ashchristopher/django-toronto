from django.contrib import admin

from .models import Event, Location


class LocationAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
