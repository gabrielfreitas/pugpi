from django.contrib import admin
from .models import Event
from .forms import EventForm


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'time')
    form = EventForm

admin.site.register(Event, EventAdmin)