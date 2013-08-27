# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

class Album(models.Model):

    titulo = models.CharField(max_length=100, help_text="Titulo do album com até 100 caracteres.")
    foto_destaque = models.ImageField(upload_to='uploads/album/%Y/%m/', help_text="Foto destaque do Album")
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    creditos = models.CharField(max_length = 150, blank = True, null = True)

    publicado_em = models.DateTimeField(verbose_name='Data de Publicação', auto_now_add= True)
    cadastrado_em = models.DateTimeField(verbose_name='Data do Cadastro', auto_now_add= True, blank=True)
    status = models.BooleanField(verbose_name='Ativo? ', default=True)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return ('/albuns/%s-%i.html' % (self.slug, self.id))


    class Meta:
        ordering = ('-cadastrado_em',)
        verbose_name = 'Álbum'
        verbose_name_plural = 'Álbuns'


class Foto(models.Model):

    album = models.ForeignKey(Album)
    foto = models.ImageField(upload_to='uploads/album/fotos/%Y/%m/')#, size=(530, 397)
    legenda = models.CharField(max_length=100, blank=True)

    cadastrado_em = models.DateTimeField(verbose_name='Data do Cadastro', auto_now_add= True, blank=True, null = True)
    status = models.BooleanField(verbose_name='Ativo? ', default=True)

    def __unicode__(self):
        return self.legenda

    def get_foto(self):
        return "/media/%s" % self.foto

    class Meta:
        ordering = ('-cadastrado_em',)

def album_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)

signals.pre_save.connect(album_pre_save, sender=Album)

