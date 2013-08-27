# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Event


def events(request):
    events = Event.objects.filter(time__gte=datetime.now()).order_by('-time')
    paginator = Paginator(events, 5)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        events = paginator.page(page)
    except(EmptyPage, InvalidPage):
        events = paginator.page(paginator.num_pages)
    return render(request, 'core/events.html', {'events': events})


def event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'core/event.html', {'event': event})