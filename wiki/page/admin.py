from django.contrib import admin

from models import Page, PageRevision

class PageRevisionAdmin(admin.TabularInline):
    model = PageRevision
    extra = 1

class PageAdmin(admin.ModelAdmin):
    model = Page
    inlines = [PageRevisionAdmin]

admin.site.register(Page, PageAdmin)
