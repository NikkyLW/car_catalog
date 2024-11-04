from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username