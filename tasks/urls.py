from django.urls import path
from . import views

urlpatterns = [
    # UI Routes
    path('', views.task_page, name='task_list'),
    path('add/', views.add_task_page, name='add_task'),
    path('update/<int:id>/', views.update_task_page, name='update_task'),
    path('delete/<int:id>/', views.delete_task_page, name='delete_task'),

    # API (optional)
    path('tasks/', views.get_tasks),
]