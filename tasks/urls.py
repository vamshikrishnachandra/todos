# tasks/urls.py
from django.urls import path
from .views import task_list, task_detail, task_create, task_update, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/<int:task_id>/', task_detail, name='task_detail'),
    path('task/create/', task_create, name='task_create'),
    path('task/update/<int:task_id>/', task_update, name='task_update'),
    path('task/delete/<int:task_id>/', task_delete, name='task_delete'),
]
