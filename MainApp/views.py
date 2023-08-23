from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets_list")
        return render(request, 'pages/add_snippet.html', {'form': form})

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

# def create_snippet(request):
#     if request.method == "POST":
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("snippets_list")
#         return render(request,'add_snippet.html',{'form': form})

def snippet_del(request, id):
    snippet = Snippet.objects.get(id=id)
    if request.method == "POST":
        snippet.delete()
        return redirect("snippets_list")
    return render(request, 'snippet_list')

