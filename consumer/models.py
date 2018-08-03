from django.db import models

# Create your models here.
from user_auth.models import User

class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'consumers'
