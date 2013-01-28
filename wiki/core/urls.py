from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('page.views',
    url(r'^$', "index"),
    url(r'^index$', "index"),
    url(r'^history$', "history"),
    url(r'^(?P<page_slug>.+|)/$', "handle_page"),
    url(r'^(?P<page_slug>.+|)/edit$', "edit_page"),
    url(r'^(?P<page_slug>.+|)/history$', "page_history"),
    url(r'^(?P<page_slug>.+|)/diff$', "diff_page")
)