from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('page.views',
    url(r'^index$', "index"),
    url(r'^(?P<page_slug>.+/|)$', "view_page")
)