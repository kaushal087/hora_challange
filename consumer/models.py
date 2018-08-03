from django.db import models

# Create your models here.
from user_auth.models import User

class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'consumers'

class ConsumerTask(models.Model):

    CREATED = 'created'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'


    STATUS_CHOICES = (
        (CREATED, CREATED),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
    )


    CLEAN_FRIDGE = 'clean fridge'
    CLEAN_ROOM = 'clean room'
    CLEAN_CAR = 'clean car'
    CLEAN_AC = 'clean AC'

    CATEGORY_CHOICES = (
        (CLEAN_AC, CLEAN_AC),
        (CLEAN_CAR, CLEAN_CAR),
        (CLEAN_FRIDGE, CLEAN_FRIDGE),
        (CLEAN_ROOM, CLEAN_ROOM)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True , max_length=300)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=300)
    status = models.CharField(choices=STATUS_CHOICES, default=CREATED,
                              null=True, blank=True, max_length=300)
    category = models.CharField(choices=CATEGORY_CHOICES, default=None,
                              null=True, blank=True, max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'consumer_tasks'
