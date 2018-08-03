


def create_task(request, data={}):
    from .models import ConsumerTask

    task = ConsumerTask.objects.create(
        user=request.user,
        description=data.get('description'),
        name=data.get('name'),
        category=data.get('category')
    )

    return task