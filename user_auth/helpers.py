from user_auth.models import User

def create_user(data={}, is_worker=False, is_consumer=False):
    user = User.objects.create_user(username=data.get('email'),
                                    email=data.get('email'),
                                    name=data.get('name'),
                                    password=data.get('password'),
                                    is_consumer=is_consumer,
                                    is_worker=is_worker)
    return user


def user_login(data={}):
    user = User.objects.create_user(username=data.get('email'),
                                    email=data.get('email'),
                                    name=data.get('name'),
                                    password=data.get('password'))





from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def worker_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='user_login'):
    '''
    Decorator for views that checks that the logged in user is a worker,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_student,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def consumer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='user_login'):
    '''
    Decorator for views that checks that the logged in user is a consumer,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_teacher,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
