from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task
import json
from django.views.decorators.csrf import csrf_exempt


# Show all tasks
@csrf_exempt
def task_page(request):
    tasks = Task.objects.all()

    # API request (Postman / JSON expected)
    if request.headers.get('Accept') == 'application/json':
        tasks_data = list(tasks.values())
        return JsonResponse(tasks_data, safe=False)

    # ✅ Case 2: Browser request (HTML page)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@csrf_exempt
def add_task_page(request):
    if request.method == 'POST':

        # JSON request (Postman)
        if request.content_type == 'application/json':
            data = json.loads(request.body)

            task = Task.objects.create(
                title=data['title'],
                description=data['description'],
                due_date=data['due_date'],
                status=data['status']
            )

            return JsonResponse({
                'message': 'Task created',
                'id': task.id
            })

        # Form request (Browser UI)
        else:
            Task.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                due_date=request.POST['due_date'],
                status=request.POST['status']
            )

            return redirect('/')


    return render(request, 'tasks/add_task.html')


@csrf_exempt
def update_task_page(request, id):
    task = Task.objects.get(id=id)

    # API (Postman - PUT request with JSON)
    if request.method == 'PUT':
        data = json.loads(request.body)

        task.title = data['title']
        task.description = data['description']
        task.due_date = data['due_date']
        task.status = data['status']
        task.save()

        return JsonResponse({
            'message': 'Task updated',
            'id': task.id
        })

    # UI (HTML form - POST request)
    elif request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.status = request.POST['status']
        task.save()

        return redirect('/')

    # GET → show form
    return render(request, 'tasks/update_task.html', {'task': task})


@csrf_exempt
def delete_task_page(request, id):
    task = Task.objects.get(id=id)

    # API request (DELETE method)
    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({
            'message': 'Task deleted',
            'id': id
        })

    # Browser request (GET)
    task.delete()
    return redirect('/')


@csrf_exempt
def get_tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe=False)