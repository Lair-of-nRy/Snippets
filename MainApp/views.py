from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserRegistrationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

@login_required
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
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
            return redirect("snippets_list")
        return render(request, 'pages/add_snippet.html', {'form': form})

def snippets_page(request):
    data = Snippet.objects.filter(public=True)
    count = data.count()
    context = {
        'snippets': data,
        'count': count
        }
    return render(request, 'pages/view_snippets.html', context)

def snippet_data(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        'pagename': 'Просмотр сниппета',
        'snippet': snippet,
        'type': 'view'
        }
    return render(request, 'pages/snippets.html', context)


def snippet_edit(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    # Хотим получить страницу данных сниппета
    if request.method == "GET":
        context = {
            'pagename': 'Редактирование сниппета',
            'snippet': snippet,
            'type': 'edit'
        }
        return render(request, 'pages/snippets.html', context)

    # Хотим создать новый Сниппет(данные от формы)
    if request.method == "POST":
        data_form = request.POST
        snippet.name = data_form["name"]
        snippet.lang = data_form["lang"]
        snippet.code = data_form["code"]
        snippet.public = data_form.get('public', False)
        snippet.creation_date = data_form["creation_date"]
        snippet.save()
        return redirect("snippets_list")




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


def login(request):
   if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           auth.login(request, user)
       else:
            context = {
                'pagename': 'PythonBin',
                'errors': ['wrong username or password']
            }
            return render(request, 'pages/index.html', context)
   return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def my_snippets(request):
    snippets = Snippet.objects.filter(user=request.user)
    count = snippets.count() 
    context = {
        'pagename': 'Мои сниппеты',
        'snippets': snippets,
        'count': count
        }
    return render(request, 'pages/view_snippets.html', context)

def create_user(request):
    context = {'pagename': 'регистрация пользователя'}
    if request.method == 'GET':
        form = UserRegistrationForm
        context['form'] = form
        return render(request, 'pages/registration.html', context)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context['form'] = form
        return render(request, 'pages/registration', context)