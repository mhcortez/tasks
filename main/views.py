from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import get_object_or_404

def task_list(request):
    tasks =Task.objects.all()
    return render(request, 'main/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'main/add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.complete = 'complete' in  request.POST #atualiza o status com base no checkbox
        task.save()
        return redirect('task_list')
        
    return render(request, 'main/edit_task.html', {'task': task})