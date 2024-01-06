from django.shortcuts import render
from django.http import Http404

from . import util


def index(request, title):

    content = util.get_entry(title)
    if content is None:
        raise Http404("Page Not Found")

    return render(request, "encyclopedia/index.html", {
        "title": title,
        "content": content
    })
