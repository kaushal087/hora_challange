from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_consumer = models.BooleanField(default=False)
    name = models.CharField(max_length=300, null=True, blank=True, default=None)

