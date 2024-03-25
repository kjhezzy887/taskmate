from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'home_text':'Welcome to Home Page'
    }
    return render(request, 'home.html', context)

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manager = request.user
            form.save()
            messages.success(request, ("New Task Added!"))
            return redirect('todolist')    
    else:    
        all_tasks = TaskList.objects.filter(manager=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks' : all_tasks})
    
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
    else:
        messages.error(request, ('Access Denied!'))
        
    return redirect('todolist')
    
    

def edit_task(request, task_id):
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance= task)
        if form.is_valid():
            form.save()
            messages.success(request, ('Task Edited!'))
            return redirect('todolist')
        else:
            obj = TaskList.objects.get(pk=task_id)
        
        return render(request, 'edit.html', {'obj': obj})
    
def task_status(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        if task.done:
            task.done = False
            task.save()
                
        else:
            task.done = True
            task.save()
    else:
        messages.error(request, ('Access Denied!'))
        
    return redirect('todolist')

def about(request):
    context = {
        'about_text':'Welcome to About Page'
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'contact_text':'Welcome to Contact Page'
    }
    return render(request, 'contact.html', context)