from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='snippets_list'),
    path('snippets/<int:id>', views.snippet_data, name='snippet'),
    path('snippets/<int:id>/delete', views.snippet_del, name='del_snippet'),
    path('snippets/<int:id>/edit', views.snippet_edit, name='edit_snippet'),
    path('snippets/my', views.my_snippets, name='my_snippets'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('auth/register', views.create_user, name='register')
    # path('snippets/create', views.create_snippet, name='snippet_create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
