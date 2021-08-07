"""task_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ToDoView, add_todo, edit_todo, update_todo, delete_todo, search_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('', HomeView.as_view(), name='Home'),
    path('todo-view/', ToDoView.as_view(), name='ToDo'),
    path('add-todo/', add_todo, name='Add-ToDo'),
    path('edit-todo/<int:id>', edit_todo, name='Edit-ToDo'),
    path('update-todo/<int:id>', update_todo, name='Update-ToDo'),
    path('delete-todo/<int:id>', delete_todo, name='Delete-ToDo'),
    path('search-task/', search_tasks, name='Search'),
]
