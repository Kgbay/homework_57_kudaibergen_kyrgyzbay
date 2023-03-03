from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from tracker.models import Task, Type, Status, TypeChoice, StatusChoice

def add_view(request: WSGIRequest):
    if request.method == "GET":
        tasks = Task.objects.all()
        context = {
            'tasks': tasks,
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
    status = Status.objects.get(status_name=task_data['status'])
    type = Type.objects.get(type_name=task_data['type'])
    Task.objects.create(summary=task_data['summary'], description=task_data['description'], status=status, type=type)
    return redirect('index')