from django.urls import path

from . import views

urlpatterns = [
    path('create-task', views.CreateTask.as_view(), name='consumer_create_task'),
    path('task-list', views.TaskList.as_view(),
         name='consumer_task_list'),
    path('completed-task-list', views.CompletedTaskList.as_view(),
         name='consumer_completed_task_list'),

    path('', views.index, name='consumer_auth_index'),


]
