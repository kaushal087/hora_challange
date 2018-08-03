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

