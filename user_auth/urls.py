from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/worker/', views.WorkerSignUpView.as_view(), name='worker_signup'),
    path('signup/consumer/', views.ConsumerSignUpView.as_view(), name='consumer_signup'),
    path('login/', views.LoginView.as_view(), name='user_login'),
    path('login/', views.LoginView.as_view(), name='user_login'),
    path('', views.logout_view, name='user_auth_logout'),
]