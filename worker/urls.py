from django.urls import path

from . import views

urlpatterns = [
    path('task-list', views.TaskList.as_view(),
         name='worker_task_list'),
    path('', views.index, name='worker_auth_index'),

]