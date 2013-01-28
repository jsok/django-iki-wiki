from django.db import models

class PageRevision(models.Model):
    """
    The contents of a page at some point in time designated by a revision number.
    """

    number = models.IntegerField(verbose_name='Revision Number')
    contents = models.TextField(verbose_name='Page Contents')
    comment = models.CharField(verbose_name='Comment', max_length=256)
    creation_date = models.DateTimeField(auto_now_add=True)

    page = models.ForeignKey('Page', related_name='revision_history')

    def previous_revision(self):
        return max(self.number - 1, 0)

    def __unicode__(self):
        return '{title} @ r{rev}'.format(rev = self.number, title=self.page.title)

    class Meta:
        get_latest_by = 'creation_date'

class Page(models.Model):
    """
    A wiki page
    """

    title = models.CharField(verbose_name='Page Title', max_length=128, null=False, blank=False)
    slug = models.SlugField(verbose_name='Page Slug', null=False, blank=False)

    current_revision = models.OneToOneField('PageRevision', related_name='current_set', null=True, blank=True)

    def next_revision(self):
        if self.current_revision:
            return self.current_revision.number + 1
        else:
            return 0

    def __unicode__(self):
        return '{title}'.format(title=self.title)

from django.forms import ModelForm, Textarea

class PageRevisionForm(ModelForm):
    class Meta:
        model = PageRevision
        fields = ('contents', 'comment')
        widgets = {
            'contents': Textarea(attrs={'cols': 120, 'rows': 20, 'class': "input-xxlarge"}),
            'comment': Textarea(attrs={'cols': 120, 'rows': 2, 'class': "input-xxlarge"}),
        }
