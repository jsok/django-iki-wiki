from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Page, PageRevision, PageRevisionForm
from utils import title_from_slug

def index(request, template_name='index.html'):
    context = {
        'pages': Page.objects.order_by('title')
    }
    return render_to_response(template_name, RequestContext(request, context))

def history(request, page_slug=None, template_name='history.html'):
    try:
        page = Page.objects.get(slug=page_slug)
        title = page.title
        revisions = page.revision_history.order_by('-creation_date')
    except Page.DoesNotExist:
        title = "Global History"
        revisions = PageRevision.objects.order_by('-creation_date')

    context = {
        'title': title,
        'revisions': revisions,
    }
    return render_to_response(template_name, RequestContext(request, context))

def handle_page(request, page_slug=None):
    try:
        page = Page.objects.get(slug=page_slug)
        return view_page(request, page)
    except Page.DoesNotExist:
        title = title_from_slug(page_slug)
        return new_page(request, title)

def new_page(request, title, template_name='page/new.html'):
    context = {
        'title': title,
    }
    return render_to_response(template_name, RequestContext(request, context))

def view_page(request, page, template_name='page/view.html'):
    context = {
        'title': page.title,
        'contents': page.current_revision.contents,
    }
    return render_to_response(template_name, RequestContext(request, context))

def edit_page(request, page_slug=None, template_name='page/edit.html'):
    title = title_from_slug(page_slug)
    try:
        page = Page.objects.get(slug=page_slug)
    except Page.DoesNotExist:
        page = Page()

    if request.method == 'POST':
        revision = PageRevision(page=page, number=page.next_revision())
        form = PageRevisionForm(request.POST, instance=revision)

        if form.is_valid():
            # Save the page, in case it is new and because a revision requires a valid Page object
            page.title = title
            page.slug = page_slug
            page.save()

            # Save the revision
            new_revision = form.save(commit=False)
            new_revision.page = page
            new_revision.number = page.next_revision()
            new_revision.save()

            # Update the page's current revision now that the new revision has been persisted
            page.current_revision = new_revision
            page.save()

            return HttpResponseRedirect("/" + page_slug)
        else:
            print form.errors

    else:
        form = PageRevisionForm(instance=page.current_revision, initial={"comment": ""})

    context = {
        'title': title,
        'form': form.as_table(),
    }
    return render_to_response(template_name, RequestContext(request, context))
