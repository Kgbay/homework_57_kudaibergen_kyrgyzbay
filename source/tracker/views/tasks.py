from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from tracker.models import Task, Type, Status, TypeChoice, StatusChoice

def add_view(request: WSGIRequest):
    if request.method == "GET":
        tasks = Task.objects.all()
        types = Type.objects.all()
        statuses = Status.objects.all()
        context = {
            'tasks': tasks,
            'types': types,
            'statuses': statuses,
            'type_choices': TypeChoice.choices,
            'status_choices': StatusChoice.choices
        }
        return render(request, 'task_create.html', context=context)
    task_data = {
        'summary': request.POST.get('summary'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'type': request.POST.get('type')
    }
    Task.objects.create(**task_data)
    return redirect('index_view')