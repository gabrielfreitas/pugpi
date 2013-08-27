from django.contrib import admin
from apps.core.models import Event
from apps.core.forms import EventForm


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'time')
    form = EventForm

admin.site.register(Event, EventAdmin)