#
#
#
from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms


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


def home_before_login(request):
    return render(request, 'todoapp/home_before_login.html')


def about(request):
    return render(request, 'todoapp/about.html')


# REGISTRATION FORM
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'todoapp/register.html', {'form': form})


# login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Add your authentication logic here, for example:
        if username == "admin" and password == "admin":
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseRedirect('login')
    else:
        # If the request method is GET, display the login page.
        return render(request, 'todoapp/login.html')


# Logout
def logout(request):
    return render(request, 'todoapp/logged_out.html')