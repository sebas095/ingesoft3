from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Inmobiliaria.views.index_page', name='index'),
    url(r'^login/$', 'Inmobiliaria.views.login_page', name='login'),
    url(r'^logout/$', 'Inmobiliaria.views.logout_page', name='logout'),
    url(r'^inicio/$', 'app.views.inicio', name='inicio'),
    url(r'^addPub/$', 'app.views.addPub', name='addPub'),
    url(r'^listPub/$', 'app.views.listPub', name='listPub'),
    url(r'^verPub/(?P<idPub>\w+)/$', 'app.views.verPub', name='verPub'),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
