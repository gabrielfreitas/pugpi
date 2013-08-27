# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from datetime import datetime
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField('Titulo', max_length=50)
    subtitle = models.CharField('Subtítulo', max_length=75)
    image = models.ImageField('Imagem', upload_to='uploads/%Y/%m/')
    text = models.TextField('Texto')
    category = models.ForeignKey('Category', related_name='posts', verbose_name='Categoria')
    author = models.ForeignKey(User, verbose_name='Autor')
    tags = TaggableManager(blank=True)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    published_at = models.DateTimeField('Data de publicação', default=datetime.now())

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return u'/%s/%s-%i.html' % (self.category.slug, self.slug, self.id)

    class Meta:
        ordering = ['-updated_at']


class Category(models.Model):
    name = models.CharField('Nome', max_length=30)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return u'/%s.html' % self.slug

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'


def post_update_time(signal, instance, sender, **kwargs):
    instance.updated_at = datetime.now()

signals.post_save.connect(post_update_time, sender=Post)