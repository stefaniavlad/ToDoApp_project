from django.shortcuts import render

tasks = [
    {
        'id': 1,
        'task': 'Sa merg la munte',
        'task_done': False,
    },
    {
        'id': 2,
        'task': 'Sa merg la mare',
        'task_done': False,
    },
    {
        'id': 3,
        'task': 'Sa invat Python',
        'task_done': True,
    }
]



def home(request):
    context = tasks
    return render(request, 'todoapp/home.html', {'tasks': tasks})

def about(request):
    return render(request, 'todoapp/about.html')