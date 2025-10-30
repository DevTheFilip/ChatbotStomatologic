from django.shortcuts import render, redirect
from django.http import Http404

# In-memory tasks (simple global list)
tasks = []

def task_list(request):
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        tasks.append({
            'id': len(tasks) + 1,
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'status': 'pending',
        })
        return redirect('task_list')
    return render(request, 'task_form.html', {'action': 'Create', 'task': {}})

def task_update(request, task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        raise Http404('Task not found')
    if request.method == 'POST':
        task['title'] = request.POST.get('title')
        task['description'] = request.POST.get('description')
        task['status'] = request.POST.get('status', 'pending')
        return redirect('task_list')
    return render(request, 'task_form.html', {'action': 'Update', 'task': task})

def task_delete(request, task_id):
    idx = next((i for i, t in enumerate(tasks) if t['id'] == task_id), None)
    if idx is not None:
        tasks.pop(idx)
    return redirect('task_list')
