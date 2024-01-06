from django.shortcuts import render
from django.http import Http404

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_detail(request, title):
    entry_content = util.get_entry(title)

    if entry_content is None:
        raise Http404("Entry Not Found")

    return render(request, "encyclopedia/entry_detail.html", {
        "title": title,
        "content": entry_content
    })
