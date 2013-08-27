# -*- coding: utf-8 -*-

from django.db import models


class Event(models.Model):
    name = models.CharField('Nome do evento', max_length=50)
    image = models.ImageField(upload_to='uploads/events/%Y/%m', blank=True)
    description = models.CharField('Descrição', max_length=100)
    full_description = models.TextField('Descrição Completa')
    time = models.DateTimeField()
    slug = models.SlugField()

    def get_absolute_url(self):
        return u'/eventos/%s.html' % self.slug

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-time']