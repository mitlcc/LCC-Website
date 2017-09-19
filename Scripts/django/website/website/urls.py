from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.index', name="home"),
    url(r'^about$', 'website.views.about', name="about"),
    url(r'^groups$', 'website.views.groups', name="groups"),
    url(r'^events$', 'website.views.events', name="events"),
    url(r'^calendar$', 'website.views.calendar', name="calendar"),
    url(r'^contact$', 'website.views.contact', name="contact"),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
