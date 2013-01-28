from django.db import models

class PageRevision(models.Model):
    """
    The contents of a page at some point in time designated by a revision number.
    """

    number = models.IntegerField(verbose_name='Revision Number')
    contents = models.TextField(verbose_name='Page Contents')

    page = models.ForeignKey('Page', related_name='revision_history')

    def __unicode__(self):
        return 'Revision {rev} of Page {title}'.format(rev = self.number, title=self.page.title)

class Page(models.Model):
    """
    A wiki page
    """

    title = models.CharField(verbose_name='Page Title', max_length=128, null=False, blank=False)
    slug = models.SlugField(verbose_name='Page Slug', null=False, blank=False)

    current_revision = models.OneToOneField('PageRevision', related_name='current_set', null=True, blank=True)

    def __unicode__(self):
        return 'Wiki Page: {title}'.format(title=self.title)