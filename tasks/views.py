from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task
import json
from django.views.decorators.csrf import csrf_exempt

# ---------------- TEMPLATE VIEWS ---------------- #

# Show all tasks
@csrf_exempt
def task_page(request):
    tasks = Task.objects.all()

    # ✅ Case 1: API request (Postman / JSON expected)
    if request.headers.get('Accept') == 'application/json':
        tasks_data = list(tasks.values())
        return JsonResponse(tasks_data, safe=False)

    # ✅ Case 2: Browser request (HTML page)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@csrf_exempt
def add_task_page(request):
    if request.method == 'POST':

        # ✅ Case 1: JSON request (Postman)
        if request.content_type == 'application/json':
            data = json.loads(request.body)

            task = Task.objects.create(
                title=data['title'],
                description=data['description'],
                due_date=data['due_date'],
                status=data['status']
            )

            return JsonResponse({
                'message': 'Task created via API',
                'id': task.id
            })

        # ✅ Case 2: Form request (Browser UI)
        else:
            Task.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                due_date=request.POST['due_date'],
                status=request.POST['status']
            )

            return redirect('/')

    # GET request → show form
    return render(request, 'tasks/add_task.html')


@csrf_exempt
def update_task_page(request, id):
    task = Task.objects.get(id=id)

    # ✅ Case 1: API (Postman - PUT request with JSON)
    if request.method == 'PUT':
        data = json.loads(request.body)

        task.title = data['title']
        task.description = data['description']
        task.due_date = data['due_date']
        task.status = data['status']
        task.save()

        return JsonResponse({
            'message': 'Task updated via API',
            'id': task.id
        })

    # ✅ Case 2: UI (HTML form - POST request)
    elif request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.status = request.POST['status']
        task.save()

        return redirect('/')

    # ✅ Case 3: GET → show form
    return render(request, 'tasks/update_task.html', {'task': task})


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import Task

@csrf_exempt
def delete_task_page(request, id):
    task = Task.objects.get(id=id)

    # ✅ Case 1: API request (DELETE method)
    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({
            'message': 'Task deleted via API',
            'id': id
        })

    # ✅ Case 2: API using POST (optional fallback)
    elif request.method == 'POST' and 'application/json' in request.content_type:
        task.delete()
        return JsonResponse({
            'message': 'Task deleted via API (POST)',
            'id': id
        })

    # ✅ Case 3: Browser request (GET)
    task.delete()
    return redirect('/')


@csrf_exempt
def get_tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe=False)