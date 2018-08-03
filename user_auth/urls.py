from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='user_auth_index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/worker/', views.WorkerSignUpView.as_view(), name='worker_signup'),
    path('signup/consumer/', views.ConsumerSignUpView.as_view(), name='consumer_signup'),
]