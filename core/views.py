from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Task


# Load Home View
class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('Login')
        else:
            data = Task.objects.filter(created_by_id=request.user)
            return render(request, self.template_name, {'data': data})


# Load ToDo View
class ToDoView(TemplateView):
    template_name = "todo.html"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('Login')
        else:
            return render(request, self.template_name)


# Add ToDo
@login_required
def add_todo(request):
    if request.method == "POST":
        try:
            title = request.POST['title']
            description = request.POST['description']
            st_dt = datetime.strptime(request.POST['start_date'], '%m/%d/%Y').strftime('%Y-%m-%d')
            end_dt = datetime.strptime(request.POST['end_date'], '%m/%d/%Y').strftime('%Y-%m-%d')
            created_by = request.user.id
            task = Task.objects.create(
                title=title,
                description=description,
                start_date=st_dt,
                end_date=end_dt,
                created_by_id=created_by
            )
            task.save()
            messages.success(request, 'Successfully added task')
            return redirect("Home")
        except Exception as e:
            messages.error(request, 'Something went wrong please try after some time.')
            return redirect("Home")


# Edit ToDo
@login_required
def edit_todo(request, id):
    try:
        task = Task.objects.get(id=id)
        return render(request, "todo.html", {'data': task})
    except Exception as e:
        messages.error(request, 'Something went wrong please try after some time.')
        return redirect("Home")


# Update ToDo
@login_required
def update_todo(request, id):
    try:
        if request.method == 'POST':
            task = Task.objects.filter(id=id)
            title = request.POST['title']
            description = request.POST['description']
            st_dt = datetime.strptime(request.POST['start_date'], '%m/%d/%Y').strftime('%Y-%m-%d')
            end_dt = datetime.strptime(request.POST['end_date'], '%m/%d/%Y').strftime('%Y-%m-%d')
            task.update(
                title=title,
                description=description,
                start_date=st_dt,
                end_date=end_dt,
            )
            messages.success(request, 'Task updated successfully.')
            return redirect('Home')
    except Exception as e:
        messages.error(request, 'Something went wrong please try after some time.')
        return redirect("Home")


# Update ToDo
@login_required
def delete_todo(request, id):
    try:
        Task.objects.filter(id=id).delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('Home')
    except Exception as e:
        messages.error(request, 'Something went wrong please try after some time.')
        return redirect("Home")


# Search List
@login_required
def search_tasks(request):
    try:
        query_string = request.GET.get('search_query')
        tasks = Task.objects.filter(title__contains=query_string, created_by_id=request.user)
        return render(request, 'index.html', {'is_search': True, 'data': tasks})
    except Exception as e:
        messages.error(request, 'Something went wrong please try after some time.')
        return redirect("Home")
