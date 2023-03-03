from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from tracker.models import Task, Type, Status, TypeChoice, StatusChoice


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })


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
    return redirect('task_view')


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.summary = request.POST.get('summary')
        task.description = request.POST.get('description')
        status = Status.objects.get(status_name=request.POST.get('status'))
        type = Type.objects.get(type_name=request.POST.get('type'))
        task.status = status
        task.type = type
        task.save()
        return redirect('task_view', pk=task.pk)
    return render(request, 'task_update.html', context={
        'task': task,
        'type_choices': TypeChoice.choices,
        'status_choices': StatusChoice.choices
    })


def remove_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_remove.html', context={'task': task})


def task_confirm_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
