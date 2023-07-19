from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm


def home(request):
    if request.method == 'POST':
        form = TasksForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = TasksForm()
            tasks = Tasks.objects.all()
            context = {'form': form, 'tasks': tasks}
            return render(request, 'todoapp/home.html', context)
    else:
        form = TasksForm()
        tasks = Tasks.objects.all()
        context = {'form': form, 'tasks': tasks}
        return render(request, 'todoapp/home.html', context)


def delete(reguest, id):
    task = Tasks.objects.get(pk=id)
    task.delete()
    return redirect('home')


def change_status(request, id):
    task = Tasks.objects.get(pk=id)
    if task.task_done:
        task.task_done = False
        task.save()
    else:
        task.task_done = True
        task.save()

    return redirect('home')


def about(request):
    return render(request, 'todoapp/about.html')