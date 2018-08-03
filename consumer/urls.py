from django.urls import path

from . import views

urlpatterns = [
    path('create-task', views.CreateTask.as_view(), name='consumer_create_task'),
    path('', views.index, name='consumer_auth_index'),

]
