# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.multimidia.models import Album
from pugpi import settings

class AlbumAdmin(admin.ModelAdmin):

    list_display = ('titulo','get_image','cadastrado_em','status')
    exclude = ('slug',)
    list_filter = ('cadastrado_em','status')
    search_fields = ['titulo']

    def get_image(self, obj):
        return "<img src='%s%s' width='100'>" % (settings.MEDIA_URL,obj.foto_destaque)
    get_image.allow_tags = True


admin.site.register(Album, AlbumAdmin)