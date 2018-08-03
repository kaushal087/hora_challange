from django.urls import path

from . import views

urlpatterns = [
    path('task-list', views.TaskList.as_view(),
         name='worker_task_list'),

    path('my-task-list', views.MyTaskList.as_view(),
         name='worker_task_accepted_list'),

    path('task-accept/<int:task_id>/', views.TaskAccept.as_view(),
         name='worker_accept_task'),

    path('', views.index, name='worker_auth_index'),

]