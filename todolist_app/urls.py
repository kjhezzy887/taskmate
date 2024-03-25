from django.urls import path
from todolist_app import views

urlpatterns = [
    path('home/delete/<task_id>', views.delete_task, name = 'delete_task'),
    path('home/edit/<task_id>', views.edit_task, name = 'edit_task'),
    path('home/status/<task_id>', views.task_status, name = 'task_status'),
]