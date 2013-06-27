from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from pugpi import settings


urlpatterns = patterns('',
    url(r'^$', 'apps.core.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)