from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from pugpi import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.news.views.index'),
    (r'^(?P<category>[\w_-]+)/(?P<slug>[\w_-]+)-(?P<post_id>\d+).html', 'apps.news.views.post'),
    (r'^eventos/(?P<slug>[\w_-]+).html', 'apps.core.views.event'),
    (r'^eventos/$', 'apps.core.views.events'),

    url(r'^admin/', include(admin.site.urls)),

    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nAllow: /", mimetype="text/plain")),
)

urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)