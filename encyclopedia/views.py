from django.shortcuts import render, redirect
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


def search_entries(request):
    query = request.GET.get('q', '').lower()
    entries = util.list_entries()
    matching_entries = [entry for entry in entries if query in entry.lower()]

    if len(matching_entries) == 1:
        return redirect('entry_detail', title=matching_entries[0])
    elif matching_entries:
        return render(request, "encyclopedia/search_results.html", {
            "query": query,
            "entries": matching_entries
        })
    else:
        raise Http404("No Matching Entries Found")
