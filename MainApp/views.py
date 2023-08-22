from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    data = Snippet.objects.all()
    count = 0
    for i in data:
        count += 1
    context = {
        'snippets': data,
        'count': count
        }
    return render(request, 'pages/view_snippets.html', context)

def snippet_data(request, id):
    snippet = Snippet.objects.get(id=id)
    context = {'snippet': snippet}
    return render(request, 'pages/snippets.html', context)
